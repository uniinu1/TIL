#Me
# N개의 자연수가 입려되면 각 자연수의 자릿수의 합 구함
# 그 합이 최대인 자연수 출력
# 자연수 자릿수  합 구하는 함수를  def digit_sum(x)로 

import sys
#sys.stdin=open("in1.txt", "rt")

T = int(input())
a = list(map(int, input().split()))
list = []
def digit_sum(v):
    answer = 0
    for n in str(v):
        answer+=int(n)
    return answer

for t in range(T):
    digit_sum(str(a[t]))
    list.append(digit_sum(str(a[t])))


print(a[list.index(max(list))])          

#answer1 
import sys
#sys.stdin=open("in1.txt", "r")

n = int(input())
a = list(map(int, input().split()))

def digit_sum(x):
    sum = 0
    while x > 0:
        sum+=x%10
        x=x//10

    return sum

max = -2147000000
for x in a:
    tot = digit_sum(x)
    if tot > max:
        max = tot
        res = x

print(res)


#answer2
import sys
#sys.stdin=open("in1.txt", "r")

n = int(input())
a = list(map(int, input().split()))

def digit_sum(x):
    sum = 0
    for i in str(x):
        sum+=int(i)
    return sum

max = -2147000000
for x in a:
    tot = digit_sum(x)
    if tot > max:
        max = tot
        res = x

print(res)
