#answer

import sys
sys.stdin=open("input.txt", "r")
n=int(input())
a=list(map(int, input().split()))
seq=[0]*n # 0 ~ n-1 인덱스까지만 사용
for i in range(n):
    for j in range(n):
        # a 값에서 마이너스를 하면서 자기 자리를 찾아가는 코드
        if(a[i]==0 and seq[j]==0):
            seq[j]=i+1
            break
        elif seq[j]==0:
            a[i]-=1

for x in seq:
    print(x, end=' ')
'''
# my answer
# 문제가 이해되지 않아 문제 설명보고 품
import sys
sys.stdin=open("D:\강의\파이썬 알고리즘 문제풀이(코딩테스트 대비)\code\section4\input_6.txt", "r")
n=int(input())
a=list(map(int, input().split()))

result = [0] * n
for i in range(1, n + 1):
    cnt = 0
    for x, y in enumerate(result):
        if cnt == a[i - 1]:
            result[x] = i
        if y == 0:
            cnt += 1
print(result)
'''
