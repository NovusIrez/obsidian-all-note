# MUHAMMAD IZHAM BIN NORHAMADI B032020039
# AHMAD SHA HERIZAM BIN TAHIR B032020009
from scapy.all import *
ans = int(input(" 1- Determine target OS\n 2- Scan range of IP\n 3- Scan range of port\n Enter a number: "))
PH=IP()
TPH=TCP()
if ans == 1:                                    # Determine the target OS
    TPH=ICMP()
    PH.dst = input("Enter target IP: ")
elif ans == 2:                                  # Scan a range of IP in subnet
    TPH=ICMP()
    PH.dst = input("Enter network address : ")
    smask = input("Enter the subnet mask in slash eg. /30\n ")
    PH.dst = PH.dst + smask
reply=sr1(PH/TPH, retry=1, timeout=1)
print(" ******************************* ")
if reply==None:
    print(" HOST UNREACHABLE")
elif ans == 1:
    print(reply.display()) # default initial TTL value for Linux/Unix is 64, and TTL value for Windows is 128
elif ans == 2:
    print(reply.summary()) # list ICMP reply of active IP address
