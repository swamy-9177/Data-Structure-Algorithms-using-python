#quick sort pick pivot element can be first or last or middle
#two ponter approach
l=[9,2,1,0,3,4]
def partition(l,beg,end):
    pi=l[beg]
    start=beg+1
    stop=end
    while True:
        while start<len(l) and l[start]<pi:
            start+=1
    
         

def quick(l,i,j):
    if i<j:
        p=partition()
        quick(l,i,p-1)
        quick(l,p+1,j)






quick(l,0,len(l)-1)
