s=input()
stack=[]
pairs={')':'(','}':'{',']':'['}
for ch in s:
    if ch in"({[":
        stack.append(ch)
    elif ch in ")}]":
        if len(stack)==0 or stack[-1]!=pairs[ch]:
            print("NO")
            exit()
            stack.pop()
    if len(stack)==0:
        print("YES")
    else:
        print("NO")

