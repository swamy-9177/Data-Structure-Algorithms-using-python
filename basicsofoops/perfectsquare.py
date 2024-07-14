'''n=25
i=5
while i*i<n:
    i+=1
if i*i==n:
    print("perfect Sqare")
else:
    print("Not perfect Sqare")'''
'''n=int(input())
j=0
l=[0 for i in range(n)]
for i in range(n):
    a=int(input())
    if a!=0:
        l[j]=a
        j+=1
    for i in l:
        print(i,end="")

'''
'''n=5
l=[int(input()) for i in range(n-1)]
c=1
fe=l[0]
for i in range(len(l)-1):
    if l[i+1]>fe:
        c+=1
print(c)'''
n=int(input())
'''p=1
while n>0:
    d=n%10
    p=p*d
    n//=10
print(p)'''
s=str(n)
p=1
for i  in s:
    p=p*int(i)
print(p)


    

