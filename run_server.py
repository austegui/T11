import subprocess
import time
import sys
import os
import psutil
import signal

def kill_process_on_port(port):
    """Kill any process using the specified port"""
    try:
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                # Get connections separately since it's not a basic attribute
                connections = proc.net_connections()
                for conn in connections:
                    if hasattr(conn, 'laddr') and isinstance(conn.laddr, tuple) and len(conn.laddr) > 1:
                        if conn.laddr[1] == port:
                            print(f"Killing process {proc.pid} using port {port}")
                            if sys.platform == 'win32':
                                subprocess.run(['taskkill', '/F', '/PID', str(proc.pid)], 
                                            stdout=subprocess.DEVNULL, 
                                            stderr=subprocess.DEVNULL)
                            else:
                                os.kill(proc.pid, signal.SIGTERM)
                            time.sleep(1)  # Give the process time to die
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
    except Exception as e:
        print(f"Error checking for processes: {e}")

def run_server():
    """Run the server with automatic restart after each call"""
    while True:
        try:
            # Kill any process using port 8000
            kill_process_on_port(8000)
            
            print("\n=== Starting server... ===")
            
            # Start the main.py server
            process = subprocess.Popen([sys.executable, "main.py"])
            
            try:
                # Wait for the process to complete
                process.wait()
            except KeyboardInterrupt:
                print("\n=== Stopping server... ===")
                process.terminate()
                try:
                    process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    process.kill()
                break
            
            print("\n=== Server stopped, restarting in 2 seconds... ===")
            time.sleep(2)
            
        except Exception as e:
            print(f"Error in run_server: {e}")
            time.sleep(2)  # Wait before retrying

if __name__ == "__main__":
    try:
        run_server()
    except KeyboardInterrupt:
        print("\n=== Stopping server manager... ===")
        sys.exit(0)