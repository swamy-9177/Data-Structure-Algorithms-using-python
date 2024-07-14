'''l=[1,2,3,4,5,0,8,9,4]
m=l[0]
for i in l:
    if i>m:
        m=i
print(m)
'''

'''l=[1,2,3,4,5,0,8,9,4]
m=l[0]
for i in range(len(l)):
    if l[i]>m:
        m=l[i]
print(m)'''
'''l=[1,2,3,4,5,0,8,9,4]
m=l[0]
for i in range(len(l)):
    if l[i]<m:
        m=l[i]
print(m)'''
#second largest element
'''l=[8,7,6,5,4]
m=l[0]
for i in range(len(l)):
    if l[i]>m:
        m=l[i]
s=min(l)
for i in range(len(l)):
    if l[i]!=m and l[i]>s:
        s=l[i]
print(s)'''
#second smallest element
'''l=[1,2,3,4,5,0,8,9,4]
m=l[0]
for i in range(len(l)):
    if l[i]<m:
        m=l[i]
s=min(l)
for i in range(len(l)):
    if l[i]!=m and l[i]>s:
        s=l[i]
print(s)
'''
''''l=[1,1,1,1,1,12,]
i=1
k=[]
for j in l:
    if j!=i:
        k.append(i)
print(k)
'''
l=[1,1,1,1,1]
j=1
k=[]
i=0
while i<len(l):
    if l[i]==j:
        l.remove(j)
        continue
    i+=1
print(l)