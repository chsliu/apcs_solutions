
chars = 'a','c','m'
L = 2
d = {}

for c in chars:
    d[str(c)] = 0

for i in range(L):
    keys = [k for k in d.keys()]
    for k in keys:
        if len(k)<i:
            continue
        for c in chars:
            newk = str(k)+str(c)
            d[newk] = 0

keys = [k for k in d.keys()]
count = 0
for k in keys:
    if len(k)==L:
        print("%s: %d"%(k,d[k]))
        count+=1

print("Total entries: ", count)

