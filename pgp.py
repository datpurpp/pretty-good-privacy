import sys

def gcd(a, b):
    """Finds the greatest common divisor (Euclidean Algorithm)."""
    while b:
        a, b = b, a % b
    return a

def generate_keypair():
    """Generates an asymmetric Public/Private keypair using safe educational primes."""
    # Using slightly larger primes so all ASCII characters (0-255) fit safely within 'n'
    p = 61
    q = 53
    
    n = p * q  # 3233 (Our mathematical ceiling)
    phi = (p - 1) * (q - 1) # 3120

    # Choose an encryption exponent 'e' coprime to phi
    e = 17
    while gcd(e, phi) != 1:
        e += 1

    # Calculate the decryption exponent 'd' (Modular Inverse)
    d = None
    for k in range(1, phi):
        if (e * k) % phi == 1:
            d = k
            break

    # Public key is (e, n), Private key is (d, n)
    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    """Encrypts text using the Public Key padlock."""
    key, n = public_key
    # Formula: Cipher = (ASCII_Value ^ e) % n
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher

def decrypt(private_key, ciphertext):
    """Decrypts data using the Private Key."""
    key, n = private_key
    # Formula: Original = (Cipher ^ d) % n
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    return ''.join(plain)

def main():
    print("=" * 60)
    print("         DYNAMIC PGP ASYMMETRIC ENCRYPTION DEMO         ")
    print("=" * 60)

    # 1. Setup the Keys
    print("\n[+] Generating security keys...")
    public_key, private_key = generate_keypair()
    print(f"  -> PUBLIC KEY  (Share Everywhere): {public_key}")
    print(f"  -> PRIVATE KEY (Keep Hidden):     {private_key}")
    print("-" * 60)

    # 2. Get User Input
    print("\n[?] Type a secret message to test the encryption framework:")
    user_message = input(">>> ")
    
    if not user_message:
        print("[-] No message entered. Exiting script.")
        return

    # 3. Perform Encryption
    print("\n[+] Locking the data with your Public Key...")
    encrypted_data = encrypt(public_key, user_message)
    print(f"  -> What a hacker sees in transit:\n     {encrypted_data}")
    print("-" * 60)

    # 4. Perform Decryption
    print("\n[+] Unlocking the data with your Private Key...")
    decrypted_data = decrypt(private_key, encrypted_data)
    print(f"  -> Restored Clear Text:\n     \"{decrypted_data}\"")
    print("=" * 60)

if __name__ == "__main__":
    main()
