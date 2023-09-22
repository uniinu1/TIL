
# my answer
#창고 정리
# 처음 든 생각 : 배열에 넣고 max, min 함수 이용해서 하나씩 하나씩 돌면 풀 수는 있는데, 조정 횟수에 따라 시간이 많이 걸릴 수 있겠다

import sys
#sys.stdin=open("input.txt", "r")
s=list(map(int, input().split()))
p=list(map(int, input().split()))

p.sort(reverse=True)

cnt = 0
mx = 0
n=140
listT = []
for i in range(s[0]):
    #최대 무게에서 한 사람분 뺌
    n = n - p[i]
    #인원 수 체크
    mx += 1
    #listT.append(p[i])
    if mx == 2 and n >= 0:
        cnt += 1
        n = 140
        mx = 0
        #listT.append("/")
    elif n < 0:
        cnt += 1
        n = 140 - p[i]
        mx = 1
        #listT.append("-")



#print(listT)
print(cnt)
# 이 문제는 정답이 맞는데 다른 예시는 정답이 아니라고 나옴

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


