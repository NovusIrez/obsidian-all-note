from scapy.all import *
# import nmap
ans = int(input(" 1- Determine target OS\n 2- Scan range of IP\n 3- Scan range of port\n Enter a number: "))
PH=IP()
TPH=TCP()
if ans == 1:
    TPH=ICMP()
    PH.dst = input("Enter target IP: ")
elif ans == 2:
    PH.dst = input("Enter network address : ")
    smask = input("Enter the subnet mask in slash eg. /30\n ")
    PH.dst = PH.dst + smask
elif ans == 3:
    PH.dst = input("Enter target IP for port scan: ")
    fp = input("Enter first port: ")
    lp = input("Enter last port: ")
    PH.dport = (fp,lp)
reply=sr1(PH/TPH, retry=1, timeout=1)
print(" ******************************* ")
if reply==None:
    print(" HOST UNREACHABLE")
elif ans == 1:
    print(reply.display()) #default initial TTL value for Linux/Unix is 64, and TTL value for Windows is 128
elif ans == 2:
    print(reply.summary())
elif ans == 3:
    print(reply.summary())
