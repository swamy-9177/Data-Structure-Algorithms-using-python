'''coins=[1,2,5,100]
n=10000
memo=[0]*(n+1)
for i in coins:
    for a in range(i,n+1):
        memo[a]=memo[a-i]+1
print(memo[n])'''
