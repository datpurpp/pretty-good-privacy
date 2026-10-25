# Pretty Good Privacy (PGP) Key Generator & Simulator 🔐

An open-source Python application designed to demonstrate and replicate how Pretty Good Privacy (PGP) key pairs work. This educational tool creates a functioning asymmetric key pair (Public Key and Private Key), allowing users to simulate message encryption, secure transit, and decryption.

## 🚀 Features
* **Key Pair Generation:** Generates a working public key for sharing and a private key for decryption.
* **Transit Masking Simulation:** Converts secret plaintext messages into unreadable numerical strings to simulate what an eavesdropper or hacker sees in transit.
* **Secure Decryption:** Uses the corresponding private key to unlock the scrambled transit data back into the original message.
* **Open Canvas Template:** Built cleanly in Python as an upgradeable project idea for beginners and advanced developers alike.

## 🧠 How the Cryptography Works
This tool simplifies and visualizes standard asymmetric cryptography principles:
* **The Public Key 🔓:** Can be shared openly. Anyone can use your public key to encrypt a message specifically for you.
* **The Private Key 🔒:** **NEVER share your private key.** It remains exclusively with the owner to unlock messages encrypted by the public key.
* **Data in Transit 🛰️:** If a third party intercepts a message while it is traveling over the network, they will only see random characters or numerical strings.

## 💻 Getting Started

### Prerequisites
Make sure you have Python installed on your system.

### Installation
1. download
   ```
2. Navigate into the project folder:
   
   cd foldername
   ```

### Running the Program
run windows powershell & run the command:

python pgp.py
```

## 🛠️ Contributing & Upgrades
This repository serves as an educational framework meant to be upgraded and developed further! Developers are welcome to fork the project to scale up its capabilities. 

Recommended areas for expansion include upgrading the math to handle industry-standard bit-lengths (like RSA 2048/4096), integrating actual block ciphers, or adding a graphical user interface (GUI). Feel free to submit a **Pull Request** with your updates!
