a=int(input())
l=list(map(int,input().split()))
num=0
for i in l:
    if i%3!=0:
        count=int(i/3+1)
        num+=count
    else:
        count=i/3
        num+=count
print(int(num))