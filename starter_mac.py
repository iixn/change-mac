import os, time, optparse, re, signal, sys, subprocess

def signal_handler(signal, frame):
    os.system("clear")
    logo()
    print('\033[1;m [\033[1;31mX\033[1;m] You pressed Ctrl+C :(')
    time.sleep(2)
    os.system("clear")
    logo()
    exit_menu()

signal.signal(signal.SIGINT, signal_handler)

#LOGO
def logo():
    print('''
  \033[1;31m  .88. .88.
  \033[1;35m 8p  q8p \033[1;33m q8 
  \033[1;35m 88  888 \033[1;33m 88 .p888q.  .p88q
  \033[1;35m 88  888 \033[1;33m 88 8     8 8     8
  \033[1;35m 88  888 \033[1;33m 88 8     8 8      
  \033[1;35m 88  888 \033[1;33m 88 8888888 8     8
  \033[1;35m 88  888 \033[1;33m 88 8     8  'p889'

     \033[1;34m Change Yo\033[1;33mur Mac Addr\033[1;32mess By \033[1;37miixn \033[1;31mVersion : \033[1;36m1.0
     
    ''')
    
    time.sleep(2)

#OPTIONS

def opciones():
    os.system('clear')
    logo()

    opcion = input('''
            \033[1;33m1. \033[1;34mChange Mac-Address
            \033[1;33m2. \033[1;34mAbout the creator
            \033[1;33m3. \033[1;34mExit

    \033[1;33mOption : ''')

    if opcion == "1":
        Change_mac()
    elif opcion == "2":
        About()
    elif opcion == "3":
        exit_menu()
    else:
        print("    \033[1;37m[\033[1;31mX\033[1;37m] \033[1;33mInvalid option!")
        time.sleep(2)
        opciones()    

def Change_mac():
    os.system("clear")
    logo()
    preguntar_nueva_direccion_mac = input('''\t\033[1;33m-Ur new mac-address must be like this = xx:xx:xx:xx:xx:xx (else the program won't work as you want)\n\t\033[1;33m-The first number must be pair\n\t\033[1;33m-The program will need your password to continue\n\n\t\033[1;33mIntroduce the new mac address > ''')
    
    subprocess.call(["sudo", "ifconfig", "eth0", "down"])
    subprocess.call(["sudo", "ifconfig", "eth0", "hw", "ether", preguntar_nueva_direccion_mac])
    subprocess.call(["sudo", "ifconfig", "eth0", "up"])
    
    pregunta = input('''   \n\033[1;33m¿Desea hacer algo más? [S/N] : ''')
    if pregunta == "s" or pregunta == "S":
        opciones()
    elif pregunta == "n" or pregunta == "N":
        exit_menu()
    else:
        print("    \033[1;37m[\033[1;31mX\033[1;37m] \033[1;33mInvalid option!")
        time.sleep(2)
        opciones()

def About():
    os.system("clear")
    logo()
    print('''   \033[1;33mHere some information about my creator : 
    \t\033[1;33mInstagram = 14.iixn
    \t\033[1;33mGithub = iixn
    \t\033[1;33mYoutube = iixn_14
    ''')
    pregunta = input('''   \033[1;33m¿Desea hacer algo más? [S/N] : ''')
    if pregunta == "s" or pregunta == "S":
        opciones()
    elif pregunta == "n" or pregunta == "N":
        exit_menu()
    else:
        print("    \033[1;37m[\033[1;31mX\033[1;37m] \033[1;33mInvalid option!")
        time.sleep(2)
        opciones()

def exit_menu():
    os.system("clear")
    logo()
    print("\033[1;33mYou are coming out....\n")
    print("\033[1;37mThanks for use change-mac, i lve yu <3")
    time.sleep(4)
    os.system("clear")
    sys.exit()
    

opciones()
