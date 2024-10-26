import tls_client
import threading
import os
import string
import random
import json
import pystyle
import requests
import time
import sys
import ctypes
import httpx
import concurrent.futures
import base64
import websocket

from colr import color
from colorama import Fore
from datetime import datetime

output_folder = f"output/{time.strftime('%Y-%m-%d %H-%M-%S')}"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

total = open('input/tokens.txt', "r", encoding="utf-8").read().splitlines()

checked = 0; success = 0 ; locked = 0; invalid = 0; errors =0

def online_token(token):
        ws = websocket.WebSocket()
        ws.connect('wss://gateway.discord.gg/?v=9&encoding=json')        
        try:
            ws_online = websocket.WebSocket()
            ws_online.connect("wss://gateway.discord.gg/?encoding=json&v=9")
            platform = sys.platform
            status_list = ["online"]
            status = random.choice(status_list)
            ws_online.send(json.dumps({
                "op": 2,
                "d": {
                    "token": token,
                    "properties": {
                        "$os": platform,
                        "$browser": "RTB",
                        "$device": f"{platform} Device",
                    },
                    "presence": {
                    "status": status,
                    "since": 0,
                    "activities": [],
                    "afk": False,
                },
            },
            "s": None,
            "t": None
            }))
        except:
            pass
        
def TitleWorkerr():
    global checked,success,locked,invalid,errors
    if sys.platform == "linux" or sys.platform == "darwin":
        pass
    else:
        ctypes.windll.kernel32.SetConsoleTitleW(f'Team-Ai  | Success+ : {success} | Locked- : {locked} | INVA : {invalid} | E! : {errors} | Task+ : {checked}/{len(total)} | discord.gg/recaptcha ')

def get_cookies():
    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.5",
        "connection": "keep-alive",
        "host": "canary.discord.com",
        "referer": "https://canary.discord.com/",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/85.8.5 (KHTML, like Gecko) Safari/85",
        "x-context-properties": "eyJsb2NhdGlvbiI6IkFjY2VwdCBJbnZpdGUgUGFnZSJ9",
        "x-debug-options": "bugReporterEnabled",
        "x-discord-locale": "en-US",
        "x-super-properties": "eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IlNhZmFyaSIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1KTSIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IFU7IFBQQyBNYWMgT1MgWDsgZGUtZGUpIEFwcGxlV2ViS2l0Lzg1LjguNSAoS0hUTUwsIGxpa2UgR2Vja28pIFNhZmFyaS84NSIsImJyb3dzZXJfdmVyc2lvbiI6IiIsIm9zX3ZlcnNpb24iOiIiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTgxODMyLCJjbGllbnRfZXZlbnRfc291cmNlIjoibnVsbCJ9",
    }
    response = requests.get(
        "https://canary.discord.com/api/v9/experiments", headers=headers
    )
    dcfduid = response.cookies.get("__dcfduid")
    sdcfduid = response.cookies.get("__sdcfduid")
    cfruid = response.cookies.get("__cfruid")
    cf_clearance = response.cookies.get("cf_clearance")
    return f"__dcfduid={dcfduid}; __sdcfduid={sdcfduid}; __cfruid={cfruid}; cf_clearance={cf_clearance}"
class Logger: 
    def Success(text):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        lock = threading.Lock()
        lock.acquire()
        print(f'{Fore.LIGHTWHITE_EX} [{current_time}] - {Fore.LIGHTGREEN_EX}SUCCESS  {Fore.LIGHTBLACK_EX}-> {text}')
        lock.release()

    def Error(text):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        lock = threading.Lock()
        lock.acquire()
        print(f'{Fore.LIGHTWHITE_EX} [{current_time}] - {Fore.RED}ERROR  {Fore.LIGHTBLACK_EX}-> {text}')
        lock.release()

    def Info(text):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        lock = threading.Lock()
        lock.acquire()
        print(f'{Fore.LIGHTWHITE_EX} [{current_time}] - {Fore.LIGHTYELLOW_EX}INFO  {Fore.LIGHTBLACK_EX}-> {text}')
        lock.release()

    def Captcha(text):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        lock = threading.Lock()
        lock.acquire()
        print(f'{Fore.LIGHTWHITE_EX} [{current_time}] - {Fore.LIGHTBLUE_EX}SOLVE  {Fore.LIGHTBLACK_EX}-> {text}')
        lock.release()
        
class Human:
    def __init__(self) -> None:
        self.client = tls_client.Session(client_identifier="chrome_120",random_tls_extension_order=True)
        proxy = open('input/proxies.txt', "r", encoding="utf-8").read().splitlines()
        self.proxies = "http://" + random.choice(proxy).replace('sessionid', str(random.randint(1327390889,1399999999)))
        self.client.proxies = self.proxies
        self.client.headers={
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            'cookie': get_cookies(),
            'origin': 'https://discord.com',
            'priority': 'u=1, i',
            'referer': 'https://discord.com/channels/@me',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'x-context-properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6IjEyMDg0NzU2MTU5OTc3MzA5MDYiLCJsb2NhdGlvbl9jaGFubmVsX2lkIjoiMTI2MzUyMjEwNDg3NjQ2NjM0NiIsImxvY2F0aW9uX2NoYW5uZWxfdHlwZSI6MH0=',
            'x-debug-options': 'bugReporterEnabled',
            'x-discord-locale': 'en-US',
            'x-discord-timezone': 'Asia/Calcutta',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjMxODMxMywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',
        
        }

    def Main(self,email,password,token,invite):
     try:
        global checked,success,locked,invalid,errors
        online_token(token)
        self.client.headers["Authorization"] = token
        r = self.client.get("https://discord.com/api/v9/users/@me/settings")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        
        if r.status_code == 401:
            print(f"{Fore.LIGHTWHITE_EX} [{current_time}] - {Fore.LIGHTYELLOW_EX}INVAILD   {Fore.LIGHTBLACK_EX}->  Token {Fore.LIGHTWHITE_EX}-> {token}")
            with open(f"{output_folder}/FUCKED.txt", "a") as f:
                    f.write(email+":"+password + ":"+token+ "\n")
                    invalid  = invalid +1
                    checked = checked +1
                    TitleWorkerr() 
                    
        elif "captcha_key" in r.text:
            Logger.Info(f'Captcha -> {Fore.LIGHTWHITE_EX}{token[:32]}')
            with open(f"{output_folder}/captcha.txt", "a") as f:
                    f.write(email+":"+password + ":"+token+ "\n") 
                    checked = checked +1
                    TitleWorkerr() 
            
        elif r.status_code ==403: 
            print(f"{Fore.LIGHTWHITE_EX} [{current_time}] - {Fore.LIGHTRED_EX}LOCKED   {Fore.LIGHTBLACK_EX}->  Token {Fore.LIGHTWHITE_EX}-> {token}")
            with open(f"{output_folder}/locked.txt", "a") as f:
                    f.write(email+":"+password + ":"+token+ "\n")
                    locked = locked +1
                    checked = checked +1
                    TitleWorkerr() 
                    
        elif r.status_code == 200:
                ses = ''.join(random.choice(string.ascii_lowercase) + random.choice(string.digits) for _ in range(16))
                res = self.client.post(f"https://discord.com/api/v9/invites/{invite}", json={'session_id': ses})
                if res.status_code == 200:
                    Logger.Success(f'Joined Server -> {invite} | {Fore.LIGHTWHITE_EX} {token[:32]} ')
                    with open(f"{output_folder}/Joined.txt", "a") as f:
                            f.write(email+":"+password + ":"+token+ "\n") 
                            checked = checked +1
                            TitleWorkerr() 
                    success =success +1
                    TitleWorkerr()
                elif "captcha_key" in res.text:
                    Logger.Info(f'Captcha -> {Fore.LIGHTWHITE_EX}{token[:32]}')
                    with open(f"{output_folder}/captcha.txt", "a") as f:
                            f.write(email+":"+password + ":"+token+ "\n") 
                            checked = checked +1
                            TitleWorkerr() 
                else:
                    Logger.Error(res.text)  
                    errors = errors +1
                    checked = checked +1
                    TitleWorkerr()    
        else: 
            Logger.Error(r.text)
            errors = errors +1
            checked = checked +1
            TitleWorkerr() 
     except Exception as e:
      Logger.Error(e)
      with open(f"{output_folder}/errors.txt", "a") as f:
                f.write(email+":"+password + ":"+token+ "\n")
                errors = errors +1
                checked = checked +1
                TitleWorkerr() 
    def st(self, thread_limit,invite):
        with open('input/tokens.txt') as file:
            auths = file.readlines()
            self.total = len(auths)
            with concurrent.futures.ThreadPoolExecutor(max_workers=thread_limit) as executor:
                futures = []
                for combo in auths:
                    combo = combo.strip()
                    email = combo.split(':')[0]
                    password = combo.split(':')[1]
                    token = combo.split(":")[2]
                    future = executor.submit(self.Main, email, password, token,invite)
                    futures.append(future)
                for future in concurrent.futures.as_completed(futures):
                    try:
                        future.result()
                    except Exception as e:
                        print(f"Error occurred in thread: {e}")


        time.sleep(3)

if __name__ == "__main__":
    os.system("cls")
    k = ("""
                              _______________    __  ___      ___    ____
                             /_  __/ ____/   |  /  |/  /     /   |  /  _/
                              / / / __/ / /| | / /|_/ /_____/ /| |  / /  
                             / / / /___/ ___ |/ /  / /_____/ ___ |_/ /   
                            /_/ /_____/_/  |_/_/  /_/     /_/  |_/___/  
                            
                            
            server = https://discord.gg/recaptcha       discord = tunable1 | Nikhil.frr
          """)
    print(pystyle.Center.XCenter(pystyle.Colorate.Vertical(text=k, color=pystyle.Colors.green_to_white), spaces=15))
    thread = input(' [INFO] Thread-> ')
    invite = input(' [INFO] Invite_code-> ')
    thread = int(thread)
    st = Human()
    st.st(thread,invite)
                    
