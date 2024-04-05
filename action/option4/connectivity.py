import json
import subprocess

def main_option4():
    json_file_path = 'configuration/conf.json'
    output_file_path = 'scan.json'

    def get_ip_from_json(json_file_path):
        try:
            with open(json_file_path) as json_file:
                data = json.load(json_file)
                target = data.get('IP')
                return target
        except Exception as e:
            print(f"Error reading JSON file: {e}")
            return None

    def check_ping(target):
        # Execute the ping command
        ping_process = subprocess.Popen(['ping', '-c', '1', target], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Wait for the process to finish
        ping_output, _ = ping_process.communicate()

        # Check the return code
        return ping_process.returncode == 0

    # Get the target IP from the JSON file
    target = get_ip_from_json(json_file_path)

    if target:
        # Use the function to check ping to a host
        if check_ping(target):
            print(f"Ping to {target} was successful!")
        else:
            print(f"Ping to {target} failed.")
    else:
        print("Target IP is not specified in the JSON file.")

# Appel de la fonction principale
main_option4()
