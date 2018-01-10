def computepay(h,r):
    if h<=40.0:
        pay=h*r
    else:
       pay=40*r+(h-40)*r*1.5
    return pay

hrs=input("Enter Hours:")
rate=input("Enter Pay Rate:")
fh=float(hrs)
fr=float(rate)

p=computepay(fh,fr)
print(p)
