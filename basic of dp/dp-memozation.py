c=0
def fib(n,memo):
    global c # no of recurrsive calls
    c+=1
    if memo[n]:
        return memo[n]
    if n==0 or n==1:
        return n
    else:
        memo[n]=fib(n-1,memo)+fib(n-2,memo)
        return memo[n]
n=int(input())
memo=[0]*(n+1)
print(fib(n,memo))
print(c)