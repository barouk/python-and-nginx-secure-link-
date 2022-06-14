#python code 


import base64
import hashlib
import calendar
import datetime

secret = "itsaSSEEECRET"
url = "/y/xx.mp4"

future = datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
expiry = calendar.timegm(future.timetuple())

secure_link = f"{secret}{url}{expiry}".encode('utf-8')

hash = hashlib.md5(secure_link).digest()
base64_hash = base64.urlsafe_b64encode(hash)
str_hash = base64_hash.decode('utf-8').rstrip('=')

print(f"http://test.com{url}?st={str_hash}&e={expiry}")




#--------------------------
#nginx config

server {
    listen  80;
    server_name _;


    location /y {
    alias /home/alireza/files/;
    # set connection secure link
    secure_link $arg_st,$arg_e;
    secure_link_md5 "itsaSSEEECRET$uri$secure_link_expires";

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

