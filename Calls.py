# Pehle ye install karein: pip install twilio
from twilio.rest import Client
import os

def start_asli_call():
    os.system('clear')
    print("\033[1;31m")
    print("  __  __  ______  _    _  _____  _____ ")
    print(" |  \/  ||  ____|| |  | ||  __ \|_   _|")
    print(" | \  / || |__   | |__| || |  | | | |  ")
    print(" | |\/| ||  __|  |  __  || |  | | | |  ")
    print(" | |  | || |____ | |  | || |__| |_| |_ ")
    print(" |_|  |_||______||_|  |_||_____/|_____|")
    
    # --- HACKER SETTINGS (Twilio Dashboard se milengi) ---
    account_sid = 'PASTE_YOUR_SID_HERE' 
    auth_token = 'PASTE_YOUR_TOKEN_HERE'
    from_number = 'PASTE_YOUR_TWILIO_NUMBER_HERE' # Jo number Twilio ne diya
    
    client = Client(account_sid, auth_token)

    victim_number = input("\n\033[1;37m[+] Enter Your Second Mobile Number: ")
    
    # Awaaz aur Message jo call par sunayi degi (TwiML)
    # Hacker yahan "OTP" maangne wali recording dalte hain
    message_to_play = "Hello Mehdi, this is a security test call. Please enter your six digit secret code now."

    print(f"\n\033[1;32m[*] MEHDI, Calling {victim_number}...")

    try:
        call = client.calls.create(
            twiml=f'<Response><Say>{message_to_play}</Say></Response>',
            to=victim_number,
            from_=from_number
        )
        print(f"\033[1;34m[✔] Call SID: {call.sid}")
        print("[!] Check your second mobile, call is coming!")
    except Exception as e:
        print(f"\033[1;31m[!] Error: {e}")
        print("\n\033[1;33m[TIP] Mehdi bhai, ye error isliye hai kyunki aapne SID aur Token nahi dala.")

start_asli_call()
