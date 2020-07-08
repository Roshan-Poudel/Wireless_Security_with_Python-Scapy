#### Note: All Python scripts of this Repository require the following requirements to be fullfilled.
## Requirements  
**Fullfill the Following requirments before executing any script of this repository:**  
a. Linux Operating System { I am using Linux Mint }    
b. Support of Network Interface Card into Monitor Mode   
c. Aircrack-ng and Scapy are required to turn NIC card into Monitor Mode and Sniff Packets respectively  
**Step 1:** Installing Aircrack-ng to turn Network Interface Card into Monitor Mode    
*sudo apt install aircrack-ng*          
**Step 2:** Installing Scapy  
*sudo apt install scapy*    
**Step 3:** Identifying Wireless Interface name:    
Type *iwconfig* in Terminal to find your Wireless Interface name. This command outputs Address of Ethernet, Loopback, Wireless Interface.My **Wireless Interface name** is *wlp3s0*. Note your **Wireless Interface name**      
# 1. Beacon_Frames_Scanner.py 
From this repository the script Beacon_Frames_Scanner.py scans and provides all the Beacons Frames Discovered by the Network Interface Card. Wireless Beacon Frames are transmitted by the Wireless Access   Points. Connection between Access Points and End Devices occur with help of Beacon Frames emitted by WLAN. Beacons Frames carry several information like Time-stamp, SSID, MAC-Addresses of Access Point, Beacon Interval, Supported Rates. Beacon frames are transmitted  periodically by Access Points to indicate their presence. Whenever we turn on the Wifi Icon in our Mobile Phone; we see lots of Wirless SSID discovered by our Phone. This is due, Access Points are emitting the Beacons Frames and our phones discover them to inform the user. Then, there further connection processes if the user wants to connect to the Access Point.  
<br/>
#### To Execute the Script:       (Note: Fullfill all necessities mentioned in Requirement Tab in Top of this Page )
git clone *https://github.com/Papu11/Wireless_Security_with_Python-Scapy.git*      
*cd Wireless_Security_with_Python-Scapy/*      
*sudo airmon-ng start <**Wireless Interface name**>*                    example: for me *sudo airmon-ng start wlp3s0*  
*sudo python2 Beacon_Frames_Scanner.py*   
 
<img src="https://github.com/Papu11/images/blob/master/1.png">  

**Start Channel Hoping:** Great, Script Started to Provide captured Beacons Frames to us. There are many Wireless Channels and changing from one channel to another is called Channel Hopping. By Default Scapy don't Support Channel Hoping So, until now we only captured the Beacon Frame of Only One Wireless Channel. At the moment our NIC card is in the Monitor Mode now, lets find our Wireless Interface name in Monitor Mode. Now, Open another terminal (ctrl + shift + N ) and type **iwconfig** Now, my Wireless interface is wlp3s0mon. **Note your new Wireless Interface name**. Lets start Channel Hoping, type sudo *airodump-ng* <**new Wireless Interface name**>  example: for me *sudo airodump-ng wlp3s0mon* . Now, Channel Hopping started and the script which is running in another Terminal is now providing the Beacon Frames of all Wireless Channel.   


<img src="https://github.com/Papu11/images/blob/master/paps.png">

# 2. Discovering_Hidden_Wifi.py      
From this repository; the script Discovering_Hidden_Wifi.py  scans and provides all the Hidden WiFi discovered by the Network Interface Card. A hidden Wireless Network doesn't broadcasts its SSID in the environment. This depicts the Access Point doesnot transmit its SSID in the Beacon Frame around the environment. The profound use of hidden wireless network is for security concerns. Hiding the network name can prevent less technically inclined people from connecting to the network. However, for a Network/Security Professionals this is just a security through obscurity. Hence, SSID can be Discovered Analyzing all Dot11 Authentication request because at some point SSID name travel in air after Sucessful Authentication.

#### To Execute the Script:   (Note: Fullfill all necessities mentioned in Requirement Tab in Top of this Page )
git clone *https://github.com/Papu11/Wireless_Security_with_Python-Scapy.git*      
*cd Wireless_Security_with_Python-Scapy/*      
*sudo airmon-ng start <**Wireless Interface name**>*                    example: for me *sudo airmon-ng start wlp3s0*  
*sudo python2 Discovering_Hidden_Wifi.py*

**Start Channel Hoping:** There are many Wireless Channels and changing from one channel to another is called Channel Hopping. By Default Scapy don't Support Channel Hoping So, until now we are in only One Wireless Channel. At the moment our NIC card is in the Monitor Mode now, lets find our Wireless Interface name in Monitor Mode. Now, Open another terminal (ctrl + shift + N ) and type **iwconfig** Now, my Wireless interface is wlp3s0mon. **Note your new Wireless Interface name**. Lets start Channel Hoping, type sudo *airodump-ng* <**new Wireless Interface name**>  example: for me *sudo airodump-ng wlp3s0mon* . Now, Channel Hopping started and the script which is running in another Terminal is now providing the Hidden Wifi Networks of all Wireless Channel.   

<img src="https://github.com/Papu11/images/blob/master/hidden.png"> 

# 3. Probes_Request_Scanner.py 
From this repository; the script Probes_Request_Scanner.py  scans and provides all the Probes Request Discovered by the Network Interface Card. Wireless Probe Requests are the packets transmitted by the Wifi clients (i.e phone, laptops etc). Probe Request contain the information about the SSID in which the device was previously connected. Lets assume that our phone connected to our Home Wifi Network with SSID "Happy Home" then whenever we are outside the range of Home Wifi Network the phone starts searching the SSID with name "Happy Home". While Searching like these previously connected wifi Network , client devices transmit a type of Packet called **Wireless Probes Request.** This is the reason why attacker suceed in Wifi Phising attack.By Analyzing Probes Request attackers find the SSID in which client devices were previously connected and setup the  Access Point with same SSID which is also called **Evil Twin Attack**. On the light of this, connecting to Unknown Wireless Networks is always a threat. This is why you should always turn off the Wifi Icon in our client devices when not in use.  

#### To Execute the Script:   (Note: Fullfill all necessities mentioned in Requirement Tab in Top of this Page )
git clone *https://github.com/Papu11/Wireless_Security_with_Python-Scapy.git*      
*cd Wireless_Security_with_Python-Scapy/*      
*sudo airmon-ng start <**Wireless Interface name**>*                    example: for me *sudo airmon-ng start wlp3s0*  
*sudo python2 Probes_Request_Scanner.py*

<img src="https://github.com/Papu11/images/blob/master/probes.png"> 

                                        Developed by: Roshan Poudel
