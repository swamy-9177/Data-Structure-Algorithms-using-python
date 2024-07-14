def tower(n,s,e,d):
    if n==1:
        print("move ",n,"from" ,s, "to", d)
        return
    tower(n-1,s,d,e)
    print("move",n,"from",s,"to",d)
    tower(n-1,e,s,d)
n=3
tower(n,"source","extra","destiny")