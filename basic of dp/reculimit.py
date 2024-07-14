import sys
sys.setrecursionlimit(100)
def fun(n):
    print(n)
    fun(n+1)
fun(1)
