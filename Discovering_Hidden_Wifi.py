from scapy.all import *
# Importing Scapy For Packet Analyzing
import datetime
# Acessing datetime for Time stamp
a=[]
# Declaring list to Append packet info into list
def hidden_AP_discovery(packet):
	# Hidden AP Detecting Function
	if packet.haslayer(Dot11Beacon):
		# Conditional Check for Dot 11 Packets
		if not packet.info:
			# If packet dont have SSID
			t=datetime.datetime.today()
			# Extracting datetime from machine
			a.append(packet.addr2)
			print( ' ' + str(len(a))+'.' + ' ' +'['+ str(t)+']' +' Hidden Wifi Detected !!'+' BSSID: ' +packet.addr2)
			# Output all the values
sniff(prn=hidden_AP_discovery,count=0)
# Continous Sniffing using Scapy Sniff Function

'''30:B5:C2:2E:6B:FC
A hidden wireless network doesn't broadcasts its SSID in the environment. The profound use of 
hidden wireless network is for security concerns. Hiding the network name can prevent less technically inclined people 
from connecting to the network, but can be discovered analyzing all Dot11 authentication request because all
SSID name travel in air if authentication is sucessful. Ultimately the SSID name need to pass through the air whenever an client completes authentication process. 
'''