# 🔑 JWTKeyCracker

**JWTKeyCracker** is a command-line tool designed to brute-force the **secret key** used to sign JSON Web Tokens (JWTs) with HMAC algorithms (HS256, HS384, HS512).  
It takes a JWT and a wordlist of potential keys and attempts to identify the correct signing secret.

---

## 🧩 How It Works
1. Splits the JWT into **header**, **payload**, and **signature**.  
2. Detects the signing algorithm from the JWT header.  
3. Iterates through the wordlist to sign the header+payload with each candidate key.  
4. Compares the generated signature to the one in the token.  
5. Prints the secret key if found.  


### ✨ Features

- 🔍 Brute-force HMAC-based JWT secrets (**HS256, HS384, HS512**)
- 📜 Custom wordlist support
- ⏱️ Execution time tracking
- 🖥️ Clean and colorful console output
`

## 🛠️ Installation

Clone the repository and ensure you have Python 3 installed:

```bash
git clone https://github.com/yourusername/JWTKeyCracker.git
cd JWTKeyCracker
```
No external libraries are required (only Python standard library).


## 🚀 Usage

```bash
python3 JWTKeyCracker.py -w <wordlist.txt> -t <JWT>
```

### Arguments

| Flag | Description                          | Required |
|------|--------------------------------------|----------|
| `-w` | Path to the wordlist containing keys | ✅       |
| `-t` | The JWT you want to crack            | ✅       |


#### Example
```bash

python3 JWTKeyCracker.py -w ./jwt_secrets.txt -t "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.KMUFsIDTnFmyG3nMiGM6H9FNFUROf3wh7SmqJp-QV30"

```

---

Created By: **Naku Tenshi**
