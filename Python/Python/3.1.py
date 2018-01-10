hrs=input("Enter Hours:")
rate=input("Enter Pay Rate:")
h=float(hrs)
r=float(rate)
if h<=40.0:
    pay=h*r
else:
   pay=40*r+(h-40)*r*1.5
print(pay)
