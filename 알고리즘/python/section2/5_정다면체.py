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

