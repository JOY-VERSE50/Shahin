

import os 
import sys
import time



logo='''\033[33m

▗▖ ▗▖▗▄▄▄▖▗▄▄▖ ▗▄▄▄▖▗▄▄▄▖
▐▌▗▞▘  █  ▐▌ ▐▌▐▌   ▐▌   
▐▛▚▖   █  ▐▛▀▚▖▐▛▀▀▘▐▛▀▀▘
▐▌ ▐▌▗▄█▄▖▐▌ ▐▌▐▙▄▄▖▐▙▄▄▖
                         
'''

def clear():
    for e in logo:
         sys.stdout.write(e)
         sys.stdout.flush()
         time.sleep(0.0010)
         
         
         
def main():
    os.system('clear')
    clear()
    print("\033[33m")
    print(40*'-')
    print("")
    print("[×] NAME        : SHAHIN HACKER    ")
    print("")
    print("[×] FACEBOOK    : FOLLOW NEXT STEP")
    print("")
    print(40*'-')
    print("")
    print("[×] [01] FACEBOOK ACCOUNT")
    print("[×] [02] EXIT")
    print("")
    ops=input('[✓] CHOOSE : ')
    if ops in ['01','1']:
       fb()
    if ops in ['02','2']:
       h='PLEASE SELECT YOUR OPTION😉'
       for char in h:
           sys.stdout.write(char)
           sys.stdout.flush()
           time.sleep(0.1)
def fb():
    print("      WAIT🫸🏻 ")
    time.sleep(0.010)
    os.system('xdg-open https://www.facebook.com/profile.php?id=100063499801479&mibextid=ZbWKwL')
    
main()                          
