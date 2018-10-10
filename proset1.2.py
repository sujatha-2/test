a=int(input())
b=int(input("value"))
c=str(a)
d=[]
for i in range(len(c)):
    d.append(c[i])
for i in range(b,len(c)):
    print(int(d[i]),end=' ')
