import base64
import os
os.remove("badreposjsonbase64.txt")
f = open("badreposjson.txt", "r")
repos = f.read()
data = base64.b64encode(repos.encode())
text_file = open("badreposjsonbase64.txt", "wb")
text_file.write(data)
text_file.close()