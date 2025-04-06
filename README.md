# JWT Secret Key Cracker
A Python script for discovering weak JWT (JSON Web Token) secret keys through brute-force attacks using a provided wordlist. This tool is designed for security researchers and developers to test the strength of JWT implementations.

## Features
- **Brute-Force Attack**: Attempts to find the secret key by generating HMAC signatures for each entry in a wordlist.
- **Multiple Algorithms**: Supports SHA-256, SHA-384, and SHA-512 hashing algorithms for signature generation.
- **Progress Tracking**: Displays real-time progress updates, including the number of attempts made.
- **Execution Time Measurement**: Reports the total execution time upon completion.

## Requirements
- Python 3.x
- Standard libraries: `os`, `argparse`, `hmac`, `base64`, `hashlib`, `time`

## Usage
To run the script, use the following command:

```bash
python3 jwt_secret_cracker.py -w <wordlist_path> -c <jwt_value> -alg <algorithm>
```
Parameters
    -w: Path to the wordlist file containing potential secret keys (required).
    -c: The JWT value to be tested (required).
    -alg: The hashing algorithm used for the JWT signature. Choose from SHA-256, SHA-384, or SHA-512 (required).

Example:
```bash
python3 jwt_secret_cracker.py -w wordlist.txt -c <your_jwt_here> -alg SHA-25
```

## Output
The script will output the following:
    Progress updates every 1000 attempts.
    A success message if the secret key is found, displaying the key and execution time.
    A failure message if the key is not found after exhausting the wordlist.

## Disclaimer
This tool is intended for educational and security research purposes only. Ensure you have explicit permission to test any JWT implementations. Unauthorized access or testing can be illegal and unethical.
