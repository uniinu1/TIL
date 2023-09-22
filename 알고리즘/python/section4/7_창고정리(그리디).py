#창고 정리
# 처음 든 생각 : 배열에 넣고 max, min 함수 이용해서 하나씩 하나씩 돌면 풀 수는 있는데, 조정 횟수에 따라 시간이 많이 걸릴 수 있겠다

import sys
sys.stdin=open("input.txt", "r")
L=int(input())
a=list(map(int, input().split()))
m=int(input())
a.sort()
for _ in range(m):
    a[0]+=1
    a[L-1]-=1
    a.sort()

print(a[L-1]-a[0])

#그냥 내 생각처럼 풀었네,,? max. min만 안 썼을 뿐
#max, min과 sort방식 시간 비교해보기
