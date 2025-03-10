import os
import requests
import socket
import subprocess
from datetime import datetime

logo = """
\033[38;2;75;0;130m████▄     ▄ ▀▄    ▄  ▄▀  ▄███▄      ▄          ▄▄▄▄▀ ████▄ ████▄ █        
\033[38;2;75;0;130m█   █ ▀▄   █  █  █ ▄▀    █▀   ▀      █      ▀▀▀ █    █   █ █   █ █       
\033[38;2;75;0;130m█   █   █ ▀    ▀█  █ ▀▄  ██▄▄    ██   █         █    █   █ █   █ █ 
\033[38;2;75;0;130m▀████  ▄ █     █   █   █ █▄   ▄▀ █ █  █        █     ▀████ ▀████ ███▄  
\033[38;2;75;0;130m      █   ▀▄ ▄▀     ███  ▀███▀   █  █ █       ▀                      ▀          
\033[38;2;75;0;130m       ▀                         █   ██                                         
\033[38;2;255;0;0mAuthor: @O2ONG \033[38;2;255;255;255m
"""

def print_option_table():
    print("\033[38;2;75;0;130m┌───────────────────────────────────────────────────────────┐")
    print("\033[38;2;75;0;130m│\033[38;2;255;255;255m [1] IP Lookup         │ [3] Port Scan      \033[38;2;75;0;130m               │")
    print("\033[38;2;75;0;130m│\033[38;2;255;255;255m [2] Webhook Sender    │ [4] Exit           \033[38;2;75;0;130m               │")
    print("\033[38;2;75;0;130m│\033[38;2;255;255;255m                       │                    \033[38;2;75;0;130m               │")
    print("\033[38;2;75;0;130m└───────────────────────────────────────────────────────────┘")

def wait_for_user():
    input("Press Enter to continue...")

def send_to_discord(webhook_url, content, botName):
    data = {
        "content": content,
        "username": botName  
    }
    
    response = requests.post(webhook_url, json=data)
    
    if response.status_code == 204:
        print("\033[38;2;0;0;255mMessage sent successfully.\033[38;2;255;255;255m")
    else:
        print(f"\033[38;2;255;0;0mFailed to send message: {response.status_code} - {response.text}")

def ping_ip(ip):
    print(f"\033[38;2;75;0;130mPinging IP: \033[38;2;255;255;255m{ip}")
    try:
        result = subprocess.run(['ping', '-n', '4', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=False)
        output = result.stdout.decode('utf-8', errors='replace')  
        print(output)
    except Exception as e:
        print(f"Ping failed: {str(e)}")

def port_scan(target_ip, ports):
    print(f"\033[38;2;75;0;130mScanning Ports for {target_ip}...\033[38;2;255;255;255m")
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(f"\033[38;2;0;255;0mPort {port} is OPEN\033[38;2;255;255;255m")
            open_ports.append(port)
        else:
            print(f"\033[38;2;255;0;0mPort {port} is CLOSED\033[38;2;255;255;255m")
        sock.close()
    return open_ports

while True:
    os.system("title OXYGEN TOOL")
    os.system("cls")
    print(logo)
    print_option_table()

    X = input("\033[38;2;75;0;130mOption: \033[38;2;255;255;255m")

    if X == "1":
        os.system("cls")
        print("\033[38;2;75;0;130mIP LOOKUP\n\033[38;2;255;255;255m")
        ip = input("Enter IP: ")
        r = requests.get(f"http://ip-api.com/json/{ip}")
        data = r.json()
        print("")
        print(f"\033[38;2;0;0;255mCountry:\033[38;2;255;255;255m {data['country']}")
        print(f"\033[38;2;0;0;255mCity:\033[38;2;255;255;255m {data['city']}")
        print(f"\033[38;2;0;0;255mRegion:\033[38;2;255;255;255m {data['regionName']}")
        print(f"\033[38;2;0;0;255mTimeZone:\033[38;2;255;255;255m {data['timezone']}")
        print("")
        wait_for_user()

    elif X == "2":
        os.system("cls")
        print("\033[38;2;75;0;130mWEBHOOK SENDER\n\033[38;2;255;255;255m")
        url = input("Webhook URL: ")
        message = input("Message: ")
        botname = input("Botname: ")
        send_to_discord(url, message, botname)
        wait_for_user()


    elif X == "3":
        os.system("cls")
        print("\033[38;2;75;0;130mPORT SCAN\n\033[38;2;255;255;255m")
        target_ip = input("Enter IP to scan: ")
    
    # Predefined list of ports
        ports = [21, 22, 23, 80, 443, 8080, 3306, 5432, 135, 445]  # Example ports
    
        open_ports = port_scan(target_ip, ports)
        print(f"\033[38;2;75;0;130mOpen Ports: \033[38;2;255;255;255m{open_ports}")
        wait_for_user()


    elif X == "4":
        print("\033[38;2;75;0;130mExiting...\033[38;2;255;255;255m")
        break
