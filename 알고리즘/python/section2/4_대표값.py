# Me
#평균(소수 첫째자리 반올림)
#N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지

import sys
#sys.stdin=open("in1.txt", "rt")

T=int(input())
a=list(map(int, input().split()))
b= []
c= []
mean = round(sum(a) / len(a))

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

maxInt = max(c)

print(mean, a.index(maxInt)+1)

# Answer

import sys
sys,stdin=opne("input.txt", "r")
n=int(input())
a=list(map(int, input().split()))
#ave = round(sum(a)/n) #파이썬에서는 round_half_even 방식이라 논리 오류 생길 수 있음
#짝수의 근사값으로 간다는 거임 4.5일때 4로 가고, 5.5일 때 6으로 감
ave = int(sum(a)/n + 0.5)

'''
- enumerate
리스트의 인덱스 값과 value를 쌍으로 가져올 수 있음
'''

min=2147000000 # 정수형의 가장 큰 수
for idx, x in enumerate(a):
    tmp=abs(x-ave)
    if tmp<min:
        min = tmp
        score = x
        res = idx+1 # 학생번호 : 0번부터 시작하니까

    elif tmp == min:
        if x > score: #점수가 같으면 이 조건에서 걸러짐(그래서 앞 번호로 선택됨)
            score=x
            res=idx+1 
 print(ave, res)
