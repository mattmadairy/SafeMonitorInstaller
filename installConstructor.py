import requests
import os 

url = 'https://raw.githubusercontent.com/mattmadairy/SafeMonitorInstaller/main/installScript' ### pull script from GitHub
resp = requests.get(url)
with open("SafeMonitorInstaller.sh", "w") as f:  ### write script to file
    f.write(resp.text)
    f.close

os.system('sudo chmod +x /home/pi/Downloads/SafeMonitorInstaller.sh') ### make script executable

os.system('/home/pi/Downloads/SafeMonitorInstaller.sh') ### execute script 