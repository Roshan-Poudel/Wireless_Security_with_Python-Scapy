#### Note: The Python scripts of this repository Requires linux Operating System and Support of Network Interface Card in Monitor Mode.

# 1. Beacon_Frames_Scanner.py 
From this repository the script Beacon_Frames_Scanner.py scans and provides all the Beacons Frames Discovered by the Network Interface Card. Wireless Beacon Frames are transmitted by the Wireless Access   Points. Connection between Access Points and End Devices occur with help of Beacon Frames emitted by WLAN. Beacons Frames carry several information like Time-stamp, SSID, MAC-Addresses of Access Point, Beacon Interval, Supported Rates. Beacon frames are transmitted  periodically by Access Points to indicate their presence. Whenever we turn on the Wifi Icon in our Mobile Phone; we see lots of Wirless SSID discovered by our Phone. This is due, Access Points are emitting the Beacons Frames and our phones discover them to inform the user. Then, there further connection processes if the user wants to connect to the Access Point.  
#### Requirements  
 Requirements to Execute the Script are:    
a. Linux Operating System { I am using Linux Mint }    
b. Support of Network Interface Card into Monitor Mode   
c. Aircrack-ng and Scapy are required to turn NIC card into Monitor Mode and Sniff Packets respectively  
**Step 1:** Installing Aircrack-ng to turn Network Interface Card into Monitor Mode    
*sudo apt install aircrack-ng*          
**Step 2:** Installing Scapy  
*sudo apt install scapy*    
**Step 3:** Identifying Wireless Interface name:    
Type *iwconfig* in Terminal to find your Wireless Interface name. This command outputs Address of Ethernet, Loopback, Wireless Interface.My **Wireless Interface name** is *wlp3s0*. Note your **Wireless Interface name**      
#### To Execute the Script:    
git clone *https://github.com/Papu11/Wireless_Security_with_Python-Scapy.git*      
*cd Wireless_Security_with_Python-Scapy/*      
*sudo airmon-ng start <**Wireless Interface name**>*                    example: for me *sudo airmon-ng start wlp3s0*  
*sudo python2 Beacon_Frames_Scanner.py*   
<img src="https://github.com/Papu11/images/blob/master/1.png">
<br/>
**Start Channel Hoping:** Great, Script Started to Provide captured Beacons Frames to us. There are many Wireless Channels and changing from one channel to another is called Channel Hopping. By Default Scapy don't Support Channel Hoping So, until now we only captured the Beacon Frame of Only One Wireless Channel. At the moment our NIC card is in the Monitor Mode now, lets find our Wireless Interface name in Monitor Mode. Now, Open another terminal (ctrl + shift + N ) and type **iwconfig** Now, my Wireless interface is wlp3s0mon. **Note your new Wireless Interface name**. Lets start Channel Hoping, type sudo *airodump-ng* <**new Wireless Interface name**>  example: for me *sudo airodump-ng wlp3s0mon* . Now, Channel Hopping started and the script which is running in another Terminal is now providing the Beacon Frames of all Wireless Channel.   


<img src="https://github.com/Papu11/images/blob/master/paps.png">


