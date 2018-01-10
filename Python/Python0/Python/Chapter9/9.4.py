fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
senders = dict()

count = 0
for line in fh:
    if line.startswith('From:'):
        words=line.split()
#        print(words[1])
#        count=count+1
        sender=words[1]
        senders[sender]=senders.get(sender,0)+1

emailer=None
mostemails=None
for sender,counts in senders.items():
    #print(sender, counts)
    if mostemails is None or counts > mostemails:
        emailer=sender
        mostemails=counts
print(emailer, mostemails)
