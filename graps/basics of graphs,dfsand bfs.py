'''class graph:
    def __init__(self):
        self.g=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    def addedge(self,a,b):
        for i in range(0,len(self.g)-1):
            for j in range(0,len(self.g[0])-1):
                if i+1==a and j+1==b:
                    self.g[a][b]=1
    def printlist(self):
        for i in self.g:
            for j in i:
                print(j,end=" ")
            print()


t=graph()
t.addedge(1,2)
t.addedge(1,4)
t.addedge(2,1)

'''
class graph:
    def __init__(self):
        self.d={}
    def addedge(self,a,b):
        if a not in self.d:
            self.d[a]=[]
            self.d[a].append(b)
        else:
            self.d[a].append(b)
    def printlist(self):
        print(self.d)
    def bfs(self,root):
        queue=[root]
        visited=[root]
        while queue:
            curr=queue.pop(0)# remove 0 for dfs
            print(curr)
            if curr in self.d:
                for i in self.d[curr]:
                    if i not in visited:
                        visited.append(i)
                        queue.append(i)




t=graph()
t.addedge(0,2)
t.addedge(1,3)
t.addedge(2,4)
t.addedge(2,5)
t.addedge(3,6)
t.addedge(3,7)
t.printlist()
t.bfs(1)
        