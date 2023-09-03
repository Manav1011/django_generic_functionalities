from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Generate an RSA key pair
private_key = rsa.generate_private_key(
    public_exponent=65537,  # Common choice for RSA
    key_size=2048,          # Choose an appropriate key size
)

# Serialize the private key to PEM format (PKCS#8)
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# Save the private key to a file (optional)
with open('/home/manav1011/Documents/django_generic_functionalities/static/keys/private_key.pem', 'wb') as private_key_file:
    private_key_file.write(private_pem)

# Extract the public key from the private key
public_key = private_key.public_key()

# Serialize the public key to PEM format (X.509)
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Save the public key to a file (optional)
with open('/home/manav1011/Documents/django_generic_functionalities/static/keys/public_key.pem', 'wb') as public_key_file:
    public_key_file.write(public_pem)