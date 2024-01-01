import subprocess
import signal

# Replace `script1.py` and `script2.py` with the actual filenames of your scripts
script1_process = subprocess.Popen(['python', 'src/sender.py'])
script2_process = subprocess.Popen(['python', 'src/receiver.py'])

# Define a signal handler function to terminate the child processes
def signal_handler(sig, frame):
    script1_process.terminate()
    script2_process.terminate()

# Register the signal handler for the SIGINT signal
signal.signal(signal.SIGINT, signal_handler)

# Wait for the child processes to finish
script1_process.wait()
script2_process.wait()
