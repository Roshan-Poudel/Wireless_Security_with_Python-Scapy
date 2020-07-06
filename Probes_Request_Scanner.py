from scapy.all import *
# importing scapy to analyze 802.11 Packets
import datetime
# Accessing datetime for timestamp
a=[]
# Opening a list to adjuest SSID
def probes_scanner(packet):
	# Opening a function Probes Scanner
	if packet.haslayer(Dot11ProbeReq):
		# Conditional statement if packet contains Probe Request
		t=datetime.datetime.today()
		a.append(packet.info)
		#Appending the SSID sent by probes request in a list
		print( ' ' + str(len(a))+'.' +'   '  +'['+ str(t)+']' + '  SSID: '+  packet.info+  '   ' 
			+ ' BSSID: ' +packet.addr2)
sniff(prn=probes_scanner,count=0)
# Continuous packet sniffing which then sents to probes_scanner function