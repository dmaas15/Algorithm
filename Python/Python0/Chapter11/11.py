import re
name = input("Enter file:")
if len(name) < 1 : name = "regex_sum_58927.txt"
sum=0
handle=open(name)
for line in handle:
    numbers=re.findall('[0-9]+',line)
    if len(numbers)>0:
        for number in numbers:
            sum=sum+int(number)
print(sum)
