import os 
import sys
import json
import hmac 
import time
import base64
import hashlib
import argparse

# --- Colors ---
red     = "\033[31m"
blue    = "\033[34m"
green   = "\033[32m"
name_bg = "\033[48;5;235m"
gray_bg = "\033[48;5;237m"

bold = "\033[1m"
reset   = "\033[0m"

def banner():
    me = f"created by: " + name_bg + red + "NakuTenshi" + reset + reset
    print(f"""
      ___          _________ _  __           _____                _              
     | \ \        / /__   __| |/ /          / ____|              | |             
     | |\ \  /\  / /   | |  | ' / ___ _   _| |     _ __ __ _  ___| | _____ _ __  
 _   | | \ \/  \/ /    | |  |  < / _ \ | | | |    | '__/ _` |/ __| |/ / _ \ '__| 
| |__| |  \  /\  /     | |  | . \  __/ |_| | |____| | | (_| | (__|   <  __/ |    
 \____/    \/  \/      |_|  |_|\_\___|\__, |\_____|_|  \__,_|\___|_|\_\___|_|    
                                       __/ |                                     
                                      |___/   {me}
        
    """                             
)

def base64url_decode(data):
    padding = '=' * (-len(data) % 4)
    data += padding
    return json.loads(base64.urlsafe_b64decode(data).decode())

def remove_lines(n: int):
    for _ in range(n):
        sys.stdout.write("\033[F")  # move cursor up
        sys.stdout.write("\033[K")  # clear line
    sys.stdout.flush()



def createJWT(data, secret) -> str:
    # data -> base64urlencode(header)+"."+base64urlencode(payload)
    # this function takes data and create signature based on that data and secret key
    # then return jwt

    rawSignature = hmac.new(secret.encode(), data.encode(), algorithm).digest()
    signature = base64.urlsafe_b64encode(rawSignature).decode().rstrip("=")
    
    return data+"."+signature


def main():
    os.system("clear")
    banner()

    print(f"<========================= {bold}Status{reset} =========================>")
    print(f"algorithm: {blue}{jwt_algorithm}{reset}")
    print(f"data: {blue}{decoded_payload}{reset}")

    x = 0 
    if os.path.exists(wordlist_path):
        with open(wordlist_path , "r") as wl:
            secrets = wl.read().split("\n")
            

            print(f"wordlist length: {blue}{len(secrets)}{reset}")

            print(f"\n<========================== {bold}logs{reset} ==========================>\n")
            start_time = time.time()
            for secret in secrets:            
                x += 1 


                remove_lines(1)
                print(f"{blue}[INFO]{reset} Scanned {x}/{len(secrets)} items")

                created_jwt = createJWT(data, secret)
                if created_jwt == JWT_value:
                    remove_lines(2)
                    end_time = time.time()
                    print(f"{green}<========================== {bold}logs{reset} {green}==========================>{reset}")

                    print("\033[32m"+"[SUCCESS]"+"\033[0m"+" the secret key is found!!")
                    print(f"secret_key: {secret}")
                    print(f"total try: {x}")
                    print(f"Execution time: {end_time-start_time}")
                    print(f"{green}<==========================================================>{reset}")
                    exit()

    else:
        print(f"{red}[ERROR]{reset} the wordList doesn't exists")
        exit()


    remove_lines(2)
    end_time = time.time()

    print(f"{red}<========================== {bold}logs{reset} {red}==========================>{reset}")
    print("\033[31m"+"[FAIL]"+"\033[0m"+" the secret key is not found")
    print(f"total try: {x}")
    print(f"Execution time: {end_time-start_time}")
    print(f"{red}<==========================================================>{reset}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", help="word list of secret keys" ,type=str , required=True)
    parser.add_argument("-t", help="the JSON WEB TOKEN" ,type=str , required=True)

    arg = parser.parse_args()
    wordlist_path = arg.w
    JWT_value = arg.t
    algorithms = {
        "HS256" : hashlib.sha256,
        "HS384" : hashlib.sha384,
        "HS512" : hashlib.sha512,
    }


    try:
        header,payload,signature = JWT_value.split(".")
        jwt_algorithm = base64url_decode(header)["alg"]
        data = header+"."+payload

        algorithm = algorithms[jwt_algorithm]
        decoded_payload = base64url_decode(payload)
    except:
        print(f"{red}[ERROR]{reset} the JWT value is not valid")
        exit()

    main()