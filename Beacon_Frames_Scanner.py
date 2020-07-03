



# !/usr/bin/python2
from scapy.all import *
# importing scapy which will help to craft packets
import datetime
# Accessing date and Time from Computer
a=[]
# Creating a list
def beacon_scanner(packet):
	if packet.haslayer(Dot11Beacon):
		# Checking if packet Contains 802.11 Beacon Layer
		t=datetime.datetime.today()
		a.append(packet.info)
		# Adding SSID names in list
		print( ' ' + str(len(a))+'.' + ' ' +'['+ str(t)+']' + '  SSID: '+  packet.info+  '  '
		 + ' BSSID: ' +packet.addr2)
sniff(prn=beacon_scanner,count=0)
# Sniffing Network Packets Continuosly using sniff function of Scapy