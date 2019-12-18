import time
from datetime import datetime as dt

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
websites = ["www.facebook.com", "facebook.com", "www.youtube.com", "youtube.com", "www.reddit.com", "reddit.com"]

counter = 0

while True:
    print("It is:")
    if dt(dt.now().hour, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().hour, dt.now().month, dt.now().day, 8):
        print("Work time")
    else:
        print("Fun time")
    time.sleep(2.5)