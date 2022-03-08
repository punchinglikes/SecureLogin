import hashlib

file = "main.py"

h = hashlib.sha1()
with open(file,'rb') as file:
    chunk = 0
    while chunk != b'':
        chunk = file.read(1024)
        h.update(chunk)
hashfile = h.hexdigest()
print(hashfile)