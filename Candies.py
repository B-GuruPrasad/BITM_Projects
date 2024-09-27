def last_candy_recipient(n,k,a):
    last_child=(a-1+k-1)%n+1
    return last_child
n,k,a=map(int,input().strip().split())
print(last_candy_recipient(n,k,a))