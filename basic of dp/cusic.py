'''arr=list(map(int,input().split()))
print(arr)
l=[]
l.append(arr[0])
n=len(arr)-1
i=1
while i!=n: 
    l.append(arr[n])
    l.append(arr[i])
    n-=1
    i+=1
print(l)'''
'''maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

solution =[[1 if i==j else 0 for j in range(len(maze[0]))]for i in range(len(maze))]

for i in solution:
    print(i)'''
'''l=[[]
for i in range(len(maze)):
    for j in range(len(maze[0])):
        maze[i][j]=0
        l.append(maze[i][j])'''
'''for i in maze:
    print(i)
'''
# Python3 implementation of the above approach
def getallpath(m, n, ans, curpath, r, c):
		if(r>=n or c>=n or r<0 or c<0 or m[r] == 0):
			return;
		
		if(r == n-1 and c == n-1):
			ans.append(curpath)
			return
		m[r] = 0
		
		# calls
		getallpath(m,n,ans,curpath+"U",r-1,c)
		getallpath(m,n,ans,curpath+"D",r+1,c)
		getallpath(m,n,ans,curpath+"L",r,c-1)
		getallpath(m,n,ans,curpath+"R",r,c+1)
		
		m[r] = 1;

# Function to store and print
# all the valid paths
def findpath(m ,n):

	# vector to store all the possible paths
	possiblePaths = []
	getallpath(m,n,possiblePaths,"",0,0)
	# Print all possible paths
	for i in range(len(possiblePaths)):
		print(possiblePaths[i], end = " ")

# Driver code
m = [ [ 1, 0, 0, 0, 0 ], 
		[ 1, 1, 1, 1, 1 ], 
		[ 1, 1, 1, 0, 1 ], 
		[ 0, 0, 0, 0, 1 ],
		[ 0, 0, 0, 0, 1 ] ]
n = len(m)
findpath(m, n)

# This code is contributed by Arpit Jain





























