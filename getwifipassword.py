import subprocess
import time
getwifi = subprocess.check_output(['netsh', 'WLAN', 'show', 'interfaces'])
data = getwifi.decode('utf-8')
ssidpart = data.find("SSID")
ssidpart += 25
bssidpart = data.find("BSSID")
fullssid = bssidpart - ssidpart
fullssid -= 6
x = 0
finalssid = ''
while x < fullssid:
    finalssid += data[(ssidpart)]
    ssidpart += 1
    x += 1
getwifipass = subprocess.check_output(['netsh', 'WLAN', 'show', 'profile', 'name=', finalssid, 'key=clear'])
passdata = getwifipass.decode('utf-8')
passpart = passdata.find("Key Content")
passpart += 25
costpart = passdata.find("Cost settings")
fullpass = costpart - passpart
fullpass -= 4
x = 0
finalpass = ''
while x < fullpass:
    finalpass += passdata[(passpart)]
    passpart += 1
    x += 1
print("SSID: "+finalssid)
print("PASS: "+finalpass)