# Uses python3
def calc_fib(n):
    count=1
    fib=[]
    fib.append(0)
    #print(fib[0])
    fib.append(1)
    #print(fib[1])
    while count< n:
        fib.append(fib[count]+fib[count-1])
        #print(fib[count+1])
        count=count+1
    return(fib[n-1])

n = int(input())
print(calc_fib(n))
