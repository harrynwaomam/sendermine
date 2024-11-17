import dkim

# Minimal email message with the From header
msg = b"From: sender@venfergusona.store\nSubject: DKIM Signing Test\n\nThis is a test message for DKIM signing."

# Path to the PKCS#1 formatted private key
private_key_path = "dkim/venfergusona_rsa.pem"

try:
    with open(private_key_path, "rb") as key_file:
        private_key = key_file.read()
except Exception as e:
    print(f"Error reading private key: {e}")
    exit(1)

# DKIM parameters
selector = b"default"
domain = b"venfergusona.store"

try:
    print("Signing the message...")
    dkim_signature = dkim.sign(
        message=msg,
        selector=selector,
        domain=domain,
        privkey=private_key,
        include_headers=[b"from", b"subject"],  # Include the 'From' header
    )
    print("DKIM Signature created successfully:")
    print(dkim_signature.decode())
except Exception as e:
    print(f"DKIM signing failed: {e}")
