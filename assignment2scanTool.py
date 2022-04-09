from scapy.all import *
import nmap
#ans=input("Enter target IP ? : ")
ans=input("1- Determine target OS\n 2- Scan range of IP\n 3- Scan range of port\n Enter a number: ")
PH=IP()
TPH=TCP()
PH.dst=input("Enter target IP: ")
if ans == 1:
    print("don't know")
elif ans == 2:
    smask = input("Enter the subnet mask in '/' eg. /30")
    PH.dst =+ smask
elif ans == 3:
    fp = input("Enter first port: ")
    lp = input("Enter last port: ")
    PH.dport = (fp,lp)
reply=sr1(PH/TPH, retry=1, timeout=1)
if reply==None:
    print(" ******************************* ")
    print(" HOST UNREACHABLE")
    print(" ******************************* ")
else :
    print(" ******************************* ")
    print(reply.summary())
    print(" ******************************* ")
