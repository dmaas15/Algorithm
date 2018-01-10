import sys
import os

fname="C:\\Code\\Vworks\\Logs\\vworks_pipette_log(24-Apr-18 9_34_21 AM).log"
fh = open(fname)
for line in fh:
    print(line.upper().rstrip())
