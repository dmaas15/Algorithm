# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
sconf=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    sconf=sconf+float(line[line.find('.'):].rstrip())
    count=count+1
print("Average spam confidence:",sconf/count)
