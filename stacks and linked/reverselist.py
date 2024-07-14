'''l=[1,2,3,4,5]
for i in range(len(l)):
    a=l.pop()
    print(a)'''
#postfrefix expressions
s="59878+-*"
st=[]
for i in s:
    if i.isdigit():
        st.append(int(i))
    elif i=="+":
        a=st.pop()
        b=st.pop()
        st.append(a+b)
    elif i=="-":
        c=st.pop()
        d=st.pop()
        st.append(abs(c-d))
    elif i=="*":
        e=st.pop()
        f=st.pop()
        st.append(e*f)
    elif i=="/":
        e=st.pop()
        f=st.pop()
        st.append(e/f)
print(st[0])