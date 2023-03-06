#!/usr/bin/python3


import random
import string
import time
from colorama import Fore, init


def header():
    head = """
██████╗  █████╗ ███████╗███████╗     ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
██╔══██╗██╔══██╗██╔════╝██╔════╝    ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██████╔╝███████║███████╗███████╗    ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██╔═══╝ ██╔══██║╚════██║╚════██║    ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
██║     ██║  ██║███████║███████║    ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                                                                                 
    """
    print(head)

my_header = header()
time.sleep(1)

def create_pass(new):
    characters = list(string.ascii_letters) + list(string.digits) + list(string.punctuation)
    passwd = []

    for i in range(1, 40):
        tmp = random.choice(characters)
        passwd.append(tmp)

    response = "".join(passwd)
    return response
while True:
    new = input("Presione enter para generar una contraseña: ")
    if new == "":
        break
    else:
        print(Fore.RED + "Por favor, pulse enter para generar la contraseña\n")    

my_pass = create_pass(new)
print("\nContraseña: ", Fore.GREEN+my_pass)

init(autoreset=True)
