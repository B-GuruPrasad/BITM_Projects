def next_prime(n):
    num=n+1
    while True:
        is_prime=True
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                is_prime=False
                break
            if is_prime:
                return num
            num+=1
n=int(input())
result=next_prime(n)
print(result)