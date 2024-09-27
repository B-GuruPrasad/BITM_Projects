N=int(input())
P=int(input())
hours=(240-P)
np=0
for i in range(1,N+1):
    if hours<i*5:
        break
    np+=1
    hours=hours-i*5
print(int(np))