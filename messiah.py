
import os
from requests import request


import os
from cryptography.fernet import Fernet
files=[]
a=os.path.split(os.getcwd())[0]

for file in os.listdir(a):
    if file== "pls-run-me.py" or file=="dont-touch-me.key" or file=="messiah.py":
        continue
    if os.path.isfile(file):
        files.append(file)

with open("dont-touch-me.key","rb") as key:
    secret_key=key.read()
secret= "jineetlundh"
userp= input("Enter Secret Phrase: ")
if userp==secret:

    for file in files:   
        with open(file,"rb") as thefile:
            contents= thefile.read()
        contents_dec= Fernet(secret_key).decrypt(contents)
        with open(file,"wb") as thefile:
            thefile.write(contents_dec)
else:
    print("Wrong Phrase")