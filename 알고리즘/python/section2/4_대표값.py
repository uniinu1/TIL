# Me
#평균(소수 첫째자리 반올림)
#N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지

import sys
#sys.stdin=open("input.txt", "rt")

T=int(input())
a=list(map(int, input().split()))
b= []
c= []
mean = round(sum(a) / len(a))
print(a)
for t in range(T):
    diff = abs(round(a[t] - mean,1))
    b.append(diff)

compare = float('inf')
for z in range(len(b)):
    if compare > b[z]:
        compare = b[z]

for z in range(len(b)):
    if compare == b[z]:
        c.append(a[z])
print(c)
maxInt = max(c)

print(mean, a.index(maxInt))

#Answer

