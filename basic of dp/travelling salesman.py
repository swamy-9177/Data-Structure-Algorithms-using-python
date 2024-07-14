map=[
    [0,10,20],
    [10,0,20],
    [30,20,0]
]
def findway(visited,pos):
    if len(visited)==len(map):
        return map[pos][0]
    mindis=float('inf')
    for city in range(len(map)):
        if city not in visited:
            newvisited=visited+[city]
            newdistance=map[pos][city]+findway(newvisited,city)
            mindis=min(mindis,newdistance)
    return mindis
visited=[0]
print(findway(visited,0))

