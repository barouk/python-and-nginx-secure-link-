#python code 


import base64
import hashlib
import calendar
import datetime

secret = "itsaSSEEECRET"
url = "/y/xx.mp4"

future = datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
expiry = calendar.timegm(future.timetuple())

secure_link = f"{secret}{url}{expiry}{ip}".encode('utf-8')

hash = hashlib.md5(secure_link).digest()
base64_hash = base64.urlsafe_b64encode(hash)
str_hash = base64_hash.decode('utf-8').rstrip('=')

print(f"http://test.com{url}?st={str_hash}&e={expiry}")




#--------------------------
#nginx config
#sudo apt install nginx-extras

server {
    listen  80;
    server_name _;


    location /t/ {
       alias /home/alireza/files/;
     }


    location /y {
    proxy_set_header X-Real-Ip $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header Host $host;
    proxy_set_header REMOTE_ADDR $remote_addr;
    sendfile on;
    tcp_nopush on;
    alias /home/alireza/files/;
    # set connection secure link
    secure_link $arg_st,$arg_e;
    secure_link_md5 "itsaSSEEECRET$uri$secure_link_expires$remote_addr";

    # bad hash
    if ($secure_link = "") {
        return 403;
    }

    # link expired
    if ($secure_link = "0") {
        return 410;
    }

    # do something useful here
}
}


#------------------------------------------
#get clint ip



import socket
## getting the hostname by socket.gethostname() method
hostname = socket.gethostname()
## getting the IP address using socket.gethostbyname() method
ip_address = socket.gethostbyname(hostname)
## printing the hostname and ip_address
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")
