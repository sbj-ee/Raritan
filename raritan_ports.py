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
