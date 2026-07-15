import requests
import os
import sys
import json
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    print("""\033[97;1m  
\x1b[1;30m~:*:\x1b[1;31m~:*:\x1b[1;32m~:*:\x1b[1;33m~:{ \x1b[1;91m\x1b[1;100m< @BlackHatFrozen   >\033[0;m\x1b[1;93m\033[97;1m }\x1b[1;30m~:*:\x1b[1;31m~:*:\x1b[1;34m~:*:\x1b[1;31m~:*:\x1b[1;32m~:*:\x1b[1;37m
\x1b[1;30m~:*:\x1b[1;31m~:*:\x1b[1;32m~:*:\x1b[1;33m~:*:\x1b[1;34m~:*::\x1b[1;30m~:*:\x1b[1;31m~:*:\x1b[1;37m~:*:\x1b[1;34m~:*:\x1b[1;39m~:*:\x1b[1;31m~:*:\x1b[1;32m~:*:\x1b[1;33m~:*:\x1b[1;37m
  \x1b[1;37m OWNER:- \x1b[1;31m @SpeakeMarin\x1b[1;37m 
   TOOL :- \x1b[1;36m Fake Information Generator
 \x1b[1;37m  INSTAGRAM :-\x1b[1;34m @prince_darkx_\x1b[1;37m
   version :- \x1b[1;33m1.0\x1b[1;37m
   TOOL :-\x1b[1;38m FREE  \x1b[1;37m   
\x1b[1;30m~:*:\x1b[1;31m~:*:\x1b[1;32m~:*:\x1b[1;33m~:*:\x1b[1;34m~:*::\x1b[1;30m~:*:\x1b[1;31m~:*:\x1b[1;37m~:*:\x1b[1;34m~:*:\x1b[1;39m~:*:\x1b[1;31m~:*:\x1b[1;32m~:*:\x1b[1;33m~:*:\x1b[1;37m
\x1b[1;30m~:*:\x1b[1;31m~:*:\x1b[1;32m~:*:\x1b[1;33m~:{ \x1b[1;91m\x1b[1;100m< Black Hat Frozen   >\033[0;m\x1b[1;93m\033[97;1m }\x1b[1;30m~:*:\x1b[1;31m~:*:\x1b[1;34m~:*:\x1b[1;31m~:*:\x1b[1;32m~:*:\x1b[1;37m
\033[1;97m""")

def fetch_from_randomuser():
    url = 'https://randomuser.me/api/?nat=id'
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    user = data['results'][0]
    name = f"{user['name']['title']} {user['name']['first']} {user['name']['last']}"
    gender = user['gender']
    location = f"{user['location']['street']['number']} {user['location']['street']['name']}, {user['location']['city']}, {user['location']['state']}, {user['location']['country']}"
    email = user['email']
    phone = user['phone']
    dob = user['dob']['date'][:10]
    return f"Name: {name}\nGender: {gender}\nAddress: {location}\nEmail: {email}\nPhone: {phone}\nDOB: {dob}"

def fetch_from_namefake():
    url = 'https://api.namefake.com/indonesian-indonesia/random/'
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    name = data.get('name', 'N/A')
    address = data.get('address', 'N/A')
    phone = data.get('phone', 'N/A')
    email = data.get('email', 'N/A')
    return f"Name: {name}\nAddress: {address}\nPhone: {phone}\nEmail: {email}"

FETCHERS = [
    fetch_from_randomuser,
    fetch_from_namefake
]

def get_fake_info():
    for fetcher in FETCHERS:
        try:
            print(f"[*] Trying {fetcher.__name__}...")
            result = fetcher()
            print("[✓] Success!")
            return result
        except Exception as e:
            print(f"[!] {fetcher.__name__} failed: {e}")
            time.sleep(1)  
    return None
def prince():
    clear_screen()
    print_banner()
    while True:
        info = get_fake_info()
        if info is None:
            print("\n[!] All APIs failed. Check your internet or try later.")
            choice = input("Press Enter to retry, or type 'exit' to quit: ").strip().lower()
            if choice == 'exit':
                break
            clear_screen()
            print_banner()
            continue
        
        print('=' * 60)
        print(info)
        print('=' * 60)
        choice = input("\nPress Enter for another, or 'exit' to quit: ").strip().lower()
        if choice == 'exit':
            break
        clear_screen()
        print_banner()

if __name__ == "__main__":
    prince()