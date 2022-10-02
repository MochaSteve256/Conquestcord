f = open("clans", "r", encoding="utf-8")
l = f.readlines()
f.close()
e = ""
for a in l:
    a = a.replace("\n", "")
    d = []
    for b in a:
        e = e + b
    d.append(e)
g = 0
print(d)
#for f in d:
    #g += int(f)
