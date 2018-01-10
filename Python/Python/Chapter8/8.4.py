fname = "romeo.txt"
fh = open(fname)
lst = list()
nst=list()
for line in fh:
    lst=line.split()
    for i in range(len(lst)):
        if not lst[i] in nst:
            nst.append(lst[i])
#for word in lst
#    if word is None
nst.sort()
print(nst)
