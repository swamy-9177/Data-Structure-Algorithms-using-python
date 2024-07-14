'''def max_score(N, K, A):
    max_score = float('-inf')

    for i in range(N - K + 1):
        window_sum = sum((j + 1) * A[j] for j in range(i, i + K))
        max_score = max(max_score, window_sum)

    return max_score

N = 5
K = 2
A = [1, 2, 3, 4, 5]
print(max_score(N, K, A))  
def max_score(N, K, A):
    max_score = float('-inf')

    for i in range(N - K + 1):
        window_sum = sum((i + j + 1) * A[i + j] for j in range(K))
        max_score = max(max_score, window_sum)

    return max_score'''
'''print(30/3)
print(30//3)'''
'''n=int(input())
l=list(map(int,input().split()))'''
n=6
l=[1,1,2,2,2,3]
print(l)
v=set(l)
print(v)
k=[]
for i in v:
    k.append(l.count(i))
print(k)
print(k.count(max(k)))
if k.count(max(k))>1:
    print(-1)
else:
    d={}
    for i in l:
        if i not in d:
             d[i]=1
        else:
            d[i]+=1
    print(d)
    m=0
    #k=-1
    k = max(zip(d.values(), d.keys()))[1]
    '''for i,j in d.items():
        if j>m:
            m=j
            k=i'''
    print(k)
