import time
from datetime import datetime as dt

hosts_path ="hosts"
# hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
websites = ["www.facebook.com", "facebook.com", "www.youtube.com", "youtube.com", "www.reddit.com", "reddit.com"]
currently_worktime = None

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        if currently_worktime == False or currently_worktime == None:
            currently_worktime = True
            with open(hosts_path, 'r+') as file:
                content = file.read()
                for website in websites:
                    if website in content:
                        pass
                    else:
                        file.write(redirect+" "+website+"\n")
            
    else:
        if (currently_worktime == True or currently_worktime == None):
            currently_worktime = False
            with open(hosts_path, 'r+') as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in websites):
                        file.write(line)
                file.truncate()
    time.sleep(60)