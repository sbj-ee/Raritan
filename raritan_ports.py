import paramiko
import time
from getpass import getpass

def connect_ssh(host, username, password, port=22):
    try:
        # Create SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the device
        print(f"Connecting to {host}...")
        ssh.connect(host, port=port, username=username, password=password)

        # Open an interactive shell session
        print("Establishing interactive shell...")
        shell = ssh.invoke_shell()

        # Wait briefly for shell to initialize
        time.sleep(1)

        # Read initial output
        output = ""
        while shell.recv_ready():
            output += shell.recv(1024).decode('utf-8')

        if output:
            print("Shell Output:")
            print(output)
            # Check if output contains "-- hit any key to accept --"
            if "-- hit any key to accept --" in output:
                print("Detected '-- hit any key to accept --', sending newline...")
                shell.send("\r\n")
                time.sleep(1)  # Wait for additional output after sending newline

                # Read additional output after sending newline
                additional_output = ""
                while shell.recv_ready():
                    additional_output += shell.recv(1024).decode('utf-8')

                if additional_output:
                    print("Additional Output after sending newline:")
                    print(additional_output)
                else:
                    print("No additional output received after sending newline")
        else:
            print("No initial output received from shell")

        # Close the shell and connection
        shell.close()
        ssh.close()
        print("Connection closed")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    # Replace these with your device details
    HOST = input("IP: ")
    USERNAME = input("User: ")
    PORT = 22  # Default SSH port

    # Prompt for password securely
    PASSWORD = getpass("Enter SSH password: ")

    connect_ssh(HOST, USERNAME, PASSWORD, PORT)
