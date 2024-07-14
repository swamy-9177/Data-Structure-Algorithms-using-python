#if list is sorted the binary search better than linear serch
l=[1,2,5,7,8,9,10]
i=0
j=len(l)-1
k=10
while i<j:
    mid=(i+j)//2
    if l[mid]==k:
        print(mid)
        break
    elif l[mid]<k:
        i=mid+1
    else:
        j=mid-1
else:
    print("not found")

