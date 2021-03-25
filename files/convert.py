import base64
import os
os.remove("badreposbase64.txt")
f = open("badrepos.txt", "r")
repos = f.read()
data = base64.b64encode(repos.encode())
text_file = open("badreposbase64.txt", "wb")
text_file.write(data)
text_file.close()