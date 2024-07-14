'''n=5
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)

'''
'''n=5
fact=1
while n>0:
    fact=fact*n
    n-=1
print(fact)'''
'''def fact(n):
    
    if  n==1:
        return 1  
    elif n==0:
        return 1 
    else:
        return fact(n-1)*n
n=int(input())
print(fact(n))'''
'''n=int(input())
l=[]
for i in range(n+1):
    l.append(i)
a=len(l)
for i in range(a):
    print(l[n])
    n-=1'''
'''n=int(input())
for i in range(n-1,0-1,-1):
    print(i)

'''
'''def rev(n):
    if n>=0:
        print(n)
        rev(n-1)
n=10
rev(n)'''
'''def sumn(N):
    s=0
    if N==1:
        return 1
    else:
        s=sumn(N-1)
        sn=N+s
        return sn


N=int(input())
print(sumn(N))
'''
l=[]
s='appanacollege'
for i in s:
    if i not in l:
        l.append(i)
print(l)
for j in l:
    print(j)





























    
