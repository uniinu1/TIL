# ()는 레이저
# 여는 괄호는 무조건 append 하기 
# 닫는 괄호를 만나면 앞의 데이터를 확인하고 앞의 데이터가 여는 괄호면 여는 괄호 pop
# append된 여는 괄호 길이가 막대기 길이임
# 이거 하면 좋을듯 다시 보면서 이해해보기


import sys
sys.stdin=open("input.txt", "r")
s=input()

stack=[]
cnt=0

for i in range(len(s)):
    if s[i]=='(':
        stack.append(s[i])
    else:
        stack.pop()
        if s[i-1]=='(':
            cnt+=len(stack)
        else:
            cnt+=1
print(cnt)

