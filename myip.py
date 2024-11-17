import requests
import socket

def get_public_ip_and_reverse_dns():
    try:
        # Fetch the public IP
        response = requests.get("https://api.ipify.org?format=text")
        if response.status_code == 200:
            public_ip = response.text
            print(f"Your current public IP address is: {public_ip}")
            
            # Perform reverse DNS lookup
            try:
                reverse_dns = socket.gethostbyaddr(public_ip)[0]
                print(f"Reverse DNS record for {public_ip}: {reverse_dns}")
            except socket.herror:
                print(f"Reverse DNS lookup failed for {public_ip}.")
        else:
            print(f"Failed to retrieve IP address. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    get_public_ip_and_reverse_dns()
