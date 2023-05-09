# 정다면체
# 나올 수 있는 눈의 합 중 가장 확률이 높은 숫자를 출력하는 프로그램
# 정답이 여러 개면 오름차순으로

import sys
#sys.stdin=open("input.txt", "rt")

list=list(map(int, input().split()))
result = []
resultFin = {}
resultFin2 = []
resultFinE = []
for a in range(list[0]):
    for b in range(list[1]):
        result.append(a+b)
        
print(result)
for c in range(len(result)):
    value = resultFin.get(result[c])
    if value == None:
        resultFin[result[c]] = result.count(result[c])
        
print(resultFin)
sorted_resultFin = sorted(resultFin.items(), key = lambda item: item[1], reverse = True)
print(sorted_resultFin)

from operator import itemgetter
print(max(sorted_resultFin,key=itemgetter(1))[1])

for x, y in sorted_resultFin:
    if y == max(sorted_resultFin,key=itemgetter(1))[1]:
        resultFin2.append(x)
resultFin2.sort()
print(*resultFin2)

# 정답이 다른 거라고 생각이 듦
#answer
# 정다면체
# 나올 수 있는 눈의 합 중 가장 확률이 높은 숫자를 출력하는 프로그램
# 정답이 여러 개면 오름차순으로

'''
해법 : 0으로 초기화한 배열에서, 더해서 나오는 값을 index로 확인, value에 1씩 더해주는 것
'''

import sys
sys.stdin=open("in1.txt", "rt")

n,m = map(int, input().split())
cnt=[0]*(n+m+3) #3은 그냥 여유치 준 것
max = -2147000000 # 가장 작은 값으로 초기화
for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j] += 1

for i in range(n+m+1):
    if cnt[i]>max:
        max-cnt[i]

for i in range(n+m+1):
    if cnt == max:
        print(i, end=' ')
