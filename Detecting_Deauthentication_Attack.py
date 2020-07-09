from scapy.all import *
import time,datetime
def detect_deauth_attack(pkt):
	if pkt.haslayer(Dot11Deauth):
		time=datetime.datetime.today()
		a= ' [ ' +  str(time)+ ' ] '+  ' Deauthentication Attack Detected Against Mac Address: ' +   str(pkt.addr2).swapcase()    
		print(a)
		log_file=open('Deauth.log','a')
		enter=a+'\n'
		log_file.write(enter)
sniff(prn=detect_deauth_attack,count=0)
