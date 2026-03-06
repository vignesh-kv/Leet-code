n,target=map(int,input().split())
arr=list(map(int,input().split()))
left=0
right=n-1
index=-1
while left<=right:
    mid=(left+right)//2
    if arr[mid]==target:
        index=mid
        break
    elif arr[mid]==target:
        index=mid
        break
    elif arr[mid]<target:
        left=mid+1
    else:
        right=mid-1
        