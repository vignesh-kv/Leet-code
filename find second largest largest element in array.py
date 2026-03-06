n=int(input())
arr=list(map(int,input().split()))
largest = -999999
second = -999999
for i in arr:
    if i>largest:
        second = largest
        largest = i
    elif i>second and i!=largest:
        second =i
    if second ==-999999:
        print(-1)
    else:
        print(second)
        

