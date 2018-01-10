# Uses python3
def calc_fib(n):
    if ((n == 0) or (n==1)):
        return n
    else:
        count=2
        fib=[]
        fib.append(1)
        fib.append(1)
        while count < n:
            fib.append((fib[count-1]+fib[count-2])%10)
            count=count+1
        return fib[count-1]

n = int(input())
print(calc_fib(n))
