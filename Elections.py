n=int(input())
a=list(map(int,input().split()))
b=set(a)
c={}
for i in b:
    c[i]=a.count(i)
max=0
for j in c.values():
    if max<j:
        max=j
d=list(c.values())
count=0
for i in d:
    if i==max:
        count+=1
if count==1:
    for key,value in c.items():
        if max==value:
            print(key)
else:
    print(-1)