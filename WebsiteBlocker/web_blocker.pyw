import time
from datetime import datetime as dt

hosts="hosts"
#Full path complies you to run command prompt as admin every time
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect='127.0.0.1'
website_list=['www.facebook.com','facebook.com','www.twitter.com','twitter.com','www.youtube.com','youtube.com']


while True:
    #Creates a datetime object based on current year,month,and day between 8AM-4PM
    if(dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,10,30)):
        print("Working Hours")
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if(website in content):
                    pass
                else:
                    file.write(redirect+' '+website+"\n")
    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun Hours")
    time.sleep(5)
