import subprocess
import sys
import argparse

def main():
    config_file = './generic_launcher_configuration.txt'
    
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Launch a command from a config file with optional arguments.")
    parser.add_argument('args', nargs=argparse.REMAINDER, help="Arguments to be appended to the command")
    
    # Parse arguments
    parsed_args = parser.parse_args()

    try:
        # Read the first line of the configuration file
        with open(config_file, 'r') as file:
            command = file.readline().rstrip('\r\n')
        
        if not command:
            print("Error: The configuration file is empty or does not contain a valid command.")
            return
        
        # Append the passed arguments to the command
        if parsed_args.args:
            command += ' ' + ' '.join(parsed_args.args)
        
        # print(f"Executing the command: {command}")

        # Execute the command
        process = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,  # Capture stdout
            stderr=subprocess.PIPE   # Capture stderr
        )
        
        # Read and separate stdout and stderr
        stdout, stderr = process.communicate()
        
        # Relay the outputs
        if stdout:
            print(stdout.decode('utf-8').rstrip('\r\n'))
        if stderr:
            print(stderr.decode('utf-8').rstrip('\r\n'), file=sys.stderr)
        
        # Print the return code
        # print(f"Process finished with exit code: {process.returncode}")
    
    except FileNotFoundError:
        print(f"Error: The file {config_file} could not be found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
