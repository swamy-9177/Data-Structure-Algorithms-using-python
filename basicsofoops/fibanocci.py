'''n=10
a=0
b=1
print(a)
print(b)
for i in range(3,n+1):
    c=a+b
    print(c)
    a=b
    b=c
'''
def fib(n):
    if n==1 or n==0:
        return 1
    else:
        return fib(n-1)+fib(n-2)
n=int(input())
print(fib(n))