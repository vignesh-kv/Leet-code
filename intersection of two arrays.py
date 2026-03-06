m,n=map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
intersection =sorted(set(arr1)&set(arr2))
if len(intersection)==0:
    print(-1)
else:
    print(*intersection)

