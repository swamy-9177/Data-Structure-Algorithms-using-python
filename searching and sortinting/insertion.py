l=[9,7,6,8,0]
for i in range(1,len(l)):
    m=l[i]
    j=i-1
    while j>-1 and m<l[j]:
        l[j+1]=l[j]
        j-=1
    l[j+1]=m
print(l)
