def count_tripllets(arr,n,m):
    unique_triplets=set()
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if arr[i]*arr[j]*arr[k]==m:
                    triplet=triplet(sorted([arr[i],arr[j],arr[k]]))
                    unique_triplets.add(triplet)
    return len(unique_triplets)
n=int(input())
arr=list(map(int,input().split()))
m=int(input())
result=count_tripllets(arr,n,m)
print(result)