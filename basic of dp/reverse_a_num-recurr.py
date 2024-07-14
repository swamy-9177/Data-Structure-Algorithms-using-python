'''n=int(input())
ans=0
 
def reverse(n,ans):
    if n==0:
        return ans
    else:
        rem=n%10
        ans=ans*10+rem
        return reverse(n//10,ans)
print(reverse(n,ans))
    '''
n=int(input())
ans=0
 
def reverse(n,ans):
    if n==0:
        print(ans)
        return ans
    else:
        rem=n%10
        ans=ans*10+rem
        reverse(n//10,ans)
print(reverse(n,ans))
    