import os 
import argparse
import hmac
import base64
import hashlib
import time 


algorithms = {
    "SHA-256" : hashlib.sha256,
    "SHA-384" : hashlib.sha384,
    "SHA-512" : hashlib.sha512,
}


parser = argparse.ArgumentParser()
parser.add_argument("-w", help="word list of secret keys" ,type=str , required=True)
parser.add_argument("-c", help="the jwt value" ,type=str , required=True)
parser.add_argument("-alg", choices=["SHA-256" , "SHA-384" , "SHA-512"] , help="the algorithm of signature of jwt" ,type=str , required=True)

arg = parser.parse_args()
wordlist_path = arg.w
JWT_value = arg.c
alg = algorithms[arg.alg]

try:
    header,payload,signature = JWT_value.split(".")
    data = header+"."+payload
except:
    print("the JWT value is not valid")

os.system("clear")
me = "created by: "+"\033[48;5;235m"+"\033[31m"+"NakuTenshi"+"\033[0m"+"\033[0m"
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


print("\033[34m"+"[INFO]"+"\033[0m"+" starting scanning...")
x = 0 
if os.path.exists(wordlist_path):
    with open(wordlist_path , "r") as wl:
        secrets = wl.read().split("\n")
        
        start_time = time.time()
        for secret in secrets:
            hmac_result = hmac.new(secret.encode(), data.encode(), alg)
            created_signature = base64.urlsafe_b64encode(hmac_result.digest()).decode().rstrip("=")
            x += 1 
            if x%1000 == 0:
                print("\033[34m"+"[INFO]"+"\033[0m"+f" {x}/{len(secrets)} is scanned")

            if created_signature == signature:
                end_time = time.time()
                print("\033[32m"+"==================================================================="+"\033[0m")
                print("\033[32m"+"[SUCCESS]"+"\033[0m"+" the secret key is found!!")
                print(f"secret_key: {secret}")
                print(f"total try: {x}")
                print(f"Execution time: {end_time-start_time}")
                print("\033[32m"+"==================================================================="+"\033[0m")
                exit()

else:
    print("the word list is not exists :(")
    exit()

end_time = time.time()
print("\033[31m"+"==================================================================="+"\033[0m")
print("\033[31m"+"[FAIL]"+"\033[0m"+" the secret key is not found")
print(f"total try: {x}")
print(f"Execution time: {end_time-start_time}")
print("\033[31m"+"==================================================================="+"\033[0m")