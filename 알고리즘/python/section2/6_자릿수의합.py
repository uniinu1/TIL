#Me
# N개의 자연수가 입려되면 각 자연수의 자릿수의 합 구함
# 그 합이 최대인 자연수 출력
# 자연수 자릿수  합 구하는 함수를  def digit_sum(x)로 

import sys
sys.stdin=open("input.txt", "rt")

T = int(input())
a = list(map(int, input().split()))
list = []
def sumFunc(v):
    answer = 0
    for n in str(v):
        answer+=int(n)
    return answer

for t in range(T):
    sumFunc(str(a[t]))
    list.append(sumFunc(str(a[t])))

list = sorted(list)
print(list)          
