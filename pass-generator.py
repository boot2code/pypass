#!/usr/bin/env python3

import random
import time
import datetime

def passcreate():
 
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums = "0123456789"
    chars = "+-/*!^#%&?"
    all = lower_case + upper_case + nums + chars

    password_length = int(input("[+] PLEASE ENTER A VALUE FOR PASSWORD LENGTH: "))
    if password_length > 100:
        print("-" * 70)
        print("[+] YOU'VE SURPASSED THE MAXIMUM PASSWORD LENGTH LIMIT.")
        print("-" * 70)
        time.sleep(2)
        quit()

    global password
    password = "".join(random.sample(all, password_length))
    print("-" * 120)
    print("[!] Your randomly generated password is ==> " + password)
    print("-" * 120)


def myfunc():
   global username
   print("-" * 70)
   username = input("[+] PLEASE ENTER YOUR AUTHORIZED USERNAME: ")
   print("-" * 70)
   if username == "root":
       print("[+] PLEASE WAIT, PASSWORD GENERATOR IS LAUNCHING...")
       print("-" * 70)
       time.sleep(3)
       passcreate()
   else:
        print("-" * 70)
        print("[+] YOU ARE NOT AUTHORIZED TO RUN THIS PROGRAM")
        print("-" * 70)
        exit()

def keeprecords():
    ts = datetime.datetime.now()
    with open('records.txt', 'a') as file:
        file.write(password +'     ' + str(ts) +'\n')
        file.close()

myfunc()
keeprecords()
