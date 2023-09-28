'''
import sys
sys.stdin=open("D:\강의\파이썬 알고리즘 문제풀이(코딩테스트 대비)\code\section5\input.txt", "rt")

s=input()
stack = []
result = ""
for i in range(len(s)):
    if s[i].isdigit():
        result += s[i]
    else:
        #연산자 우선 순위 어떻게 확인할지 몰라서 강의 확인
        print('?')
'''
#answer
import sys
sys.stdin=open("D:\강의\파이썬 알고리즘 문제풀이(코딩테스트 대비)\code\section5\input.txt", "rt")

a=input()
stack=[]
res=''
for x in a:
    if x.isdecimal():
        res += x
    else:
        if x == '(':
            stack.append(x)
        elif x == '*' or x == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(x)
        elif x==')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()

while stack:
    res += stack.pop()

print(res)
