import requests
import socket
import os

def get_rdns():
    try:
        # Get the public IP address
        response = requests.get('https://api.ipify.org')
        public_ip = response.text.strip()

        # Resolve the reverse DNS
        rdns = socket.gethostbyaddr(public_ip)[0]
        return rdns
    except Exception as e:
        print(f"Failed to obtain RDNS: {e}")
        return None

def write_rdns_to_file(rdns):
    resources_dir = "resources"
    if not os.path.exists(resources_dir):
        os.makedirs(resources_dir)
    
    file_path = os.path.join(resources_dir, "dynamic_hostname.txt")
    try:
        with open(file_path, 'w') as file:
            file.write(rdns)
        print(f"RDNS value written to {file_path}")
    except Exception as e:
        print(f"Failed to write RDNS to file: {e}")

# Run the functions
rdns = get_rdns()
if rdns:
    write_rdns_to_file(rdns)