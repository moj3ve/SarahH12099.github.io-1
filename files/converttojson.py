import os
os.remove("badreposjson.txt")
f = open("badrepos.txt", "r")
text_file = open("badreposjson.txt", "wb")
startformat = '[\n\t[\n'.encode()
text_file.write(startformat)
x = int("0")
y = int("0")
z = int("0")
with open("badrepos.txt", "r") as f:
    for line in f:
        l = []
        line = line.strip('\n')
        l.append('\t\t"')
        l.append(line)
        l.append('"')
        y += 1
        if y == 1:
            l.append(',')
        if y == 2:
            l.append(',')
        if y == 3:
            l.append(',')
        if y == 4:
            y -= 4
        l.append('\n')
        test = ''.join(l).encode()
        text_file.write(test)
        x += 1
        if x == 4:
            endformat = '\t],\n\t[\n'.encode()
            text_file.write(endformat)
            x -= 4
    ending = ']'.encode()
    text_file.write(ending)
    text_file.close()
with open("badreposjson.txt", "r") as g:
    lines = g.readlines()
    for line in g:
        z += 1
del lines[z-3]
del lines[z-2]
del lines[z-1]
with open("badreposjson.txt", "w") as h:
    for line in lines:
        h.write(line)
    endingone = str('\t]\n')
    endingtwo = str(']')
    h.write(endingone)
    h.write(endingtwo)