'''n=int(input())
for i in range(2,n):
    if n%i==0:
        print("not prime")
        break
else:
    print("prime")'''
'''n=int(input())
for i in range(2,n//2):
    if n%i==0:
        print("not prime")
        break
else:
    print("prime")'''
import math as m
n=int(input())
for i in range(2,int(m.sqrt(n))):
    if n%i==0:
        print("not prime")
        break
else:
    print("prime")
 



