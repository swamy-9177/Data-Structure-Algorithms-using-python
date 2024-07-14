#linear search
l=[8,7,9,5,2,1,0]
key=2
for i in l:
    if i==key:
        print("found")
        break
else:
    print("not found")