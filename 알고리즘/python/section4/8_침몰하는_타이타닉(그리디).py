'''
# my answer
import sys
sys.stdin=open("D:\강의\파이썬 알고리즘 문제풀이(코딩테스트 대비)\code\section4\input_6.txt", "r")
n, weight = map(int, input().split())
p=list(map(int, input().split()))

p.sort(reverse=True)

cnt = 0
listT = []
minA = min(p)
while p:
    print(p)
    if p[0] + minA <= weight:
        cnt += 1
        minIndex = p.index(minA)
        print(minIndex)
        p.pop(0)
        p.pop(minIndex)
        if p:
            minA = min(p)
    else:
        cnt += 1
        p.pop(0)

#print(listT)
print(cnt)
# case3, 4 에러

'''
#answer
#승객의 몸무게를 오름차순
#가장 가벼운 사람과 가장 무거운 사람을 더하여 확인
#몸무게가 넘어가면 마지막 사람은 혼자 타게 카운트하고, pop
#몸무게가 안 넘어가면 카운트하고 두 사람 모두 pop
import sys
from collections import deque

sys.stdin=open("input.txt", "r")
n, limit=map(int, input().split())
p=list(map(int, input().split()))
p.sort()

#list는 pop으로 앞을 빼면 계속 다시 앞으로 요소를 당기는 연산을 해서 비효율적일 수 있음(요소가 계속 움직이므로)
#deque는 요소를 가리키는 지점만 달라지는거라 pop과 같은 요소 자리 변경 연산을 하지 않음
p=deque(p)
cnt=0

#p가 다 빌 때까지
while p:
    if len(p)==1:
        cnt+=1
        break
    if p[0]+p[-1]>limit:
        p.pop()
        cnt+=1
    else:
        p.popleft()
        # list에선 p.pop(0) 써야 0번 인덱스 값 pop됨
        p.pop()
        cnt+=1
print(cnt)
