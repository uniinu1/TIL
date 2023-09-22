# 스택 : LIFO
# 파이썬에서는 스택이라는 자료구조를 따로 가지고 있는게 아니라 리스트를 POP. APPEND시키면서 스택으로 사용하는 것
#제일 처음거는 그냥 넣고 그 다음 수와 비교
# 다 하고 나면 내림차순임. 제거해야하는 수가 남으면 마지막거 지움



import sys
sys.stdin=open("input.txt", "rt")
num, m=map(int, input().split())
#붙어있는 수를 각각 리스트로 만들어주는 법
num=list(map(int, str(num)))

stack=[]

for x in num:
    #stack 비어있으면 바로 거짓됨
    # 빼낼 수 있다면 WHILE문 돌면서 계속 빼면 됨
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m-=1
    stack.append(x)

#for문 돌면서 다 못 지웟을 때 
if m!=0:
    stack=stack[:-m]
res=''.join(map(str, stack))
print(res)


