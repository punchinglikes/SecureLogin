import requests
import hashlib

api = "http://localhost:5000"
clear = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
print("Verifying Files")
h = hashlib.sha1()
with open("main.py",'rb') as file:
    chunk = 0
    while chunk != b'':
        chunk = file.read(1024)
        h.update(chunk)
hashfile = h.hexdigest()
#print(hashfile)
r = requests.get(url = api + "/hash?token=" + hashfile) #add a secret code at some point

if r.text == "confirmed": 
    print("hash confirmed")
else:
    print("hash invalid. You might be on the wrong version or may be using a modified client.")
    quit()

print(clear)
print("################")
print("# Login Screen #")
print("################")
print("\n\n")
print("1] Login")
print("2] Register")
print("3] Quit")
print("\n\n")
login_screen = int(input("==> "))

if login_screen == 1:
    print("todo")
    quit()
elif login_screen == 2:
    print("todo 2")
    quit()
elif login_screen == 3:
    print("Quitting, goodbye!")
    quit()
