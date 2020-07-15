import time
from datetime import datetime as dt

hosts_temp="hosts"
hosts_path=r"C:\Windows\System32\drivers\etc"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,0) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,3):
         print("woking hours.....")
         with open(hosts_temp,'r+') as file:
             content=file.read()
             for website in website_list:
                 if website in content:
                     pass
                 else:
                    file.write(redirect+" "+ website+"\n")
    else:
        print("fun hours.....")
    time.sleep(5)
