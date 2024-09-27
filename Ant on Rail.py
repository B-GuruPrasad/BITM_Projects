n=int(input())
l=list(map(int,input().split()))
cnt=0
c=0
for i in l:
    cnt=cnt+i
    if cnt==0:
        c=c+1
print(c)