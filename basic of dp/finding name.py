wordbank=[['a','b','c','d','e'],
          ['c','i','d','e','i'],
          ['u','j','e','n','r']
          ['r','q','h','d','w']
          ['w','q','e','f','v','s']]
word="bijen"
n=len(word)
def find(row,col,i,n,path):
    if i==n:
        print("valid")
        print(path)
        return True
    if i<0 or i>=n or j<0 or j>=n:
        return False
    if wordbank[row][col]==word[i]:
        if find(row+1,col,i+1,n,path):
            return True
        if find(row-1,col,i+1,n,path):
            return True

path=[]
for i in range(wordbank):
