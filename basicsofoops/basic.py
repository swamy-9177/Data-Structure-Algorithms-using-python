'''n=int(input())
sum=0
rem=0
while n>0:
    rem=n%10
    sum=sum+rem              # print(rem)#multiplication also by sum=1 and 
    n=n//10
print(sum)'''
'''n=int(input())
sumeven=0
sumodd=0
while n>0:
    rem=n%10
    if rem%2==0:
        sumeven=sumeven+rem
    else:
        sumodd=sumodd+rem            # print(rem)#multiplication also by sum=1 and 
    n=n//10
print(sumeven)
print(sumodd)'''
'''n=int(input())
c=0
while n>0:
    rem=n%10
    c+=1             # print(rem)#multiplication also by sum=1 and 
    n=n//10
print(c)'''
n=int(input())
n1=n
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem              
    n=n//10
if rev==n1:
    print("It is Palindrome")
else :
    print("it is not a palindrome")








