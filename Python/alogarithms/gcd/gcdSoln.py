# Uses python3
import sys

def gcd(a, b):

    while ((a!=1) or (b!=0)):
        if b==0:
            break
        r=a % b
        a=b
        b=r
    return a

if __name__ == "__main__":
    input = input()
    a, b = map(int, input.split())
    print(gcd(a, b))
