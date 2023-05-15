# my answer

# 점수 계산

'''
문제 설명
- 연속적으로 답을 맞히는 경우는 가산점을 주기 위해 다음과 같은 계산을 함
- 1번 문제가 맞는 겨웅에는 1점으로 계산. 앞의 문제에 대해서는 답을 틀리다가
답이 맞는 처음 문제는 1점으로 계산
- 연속으로 문제의 답이 맞는 경우에서 두 번째 문제는 2점, 세 번째 문제는 3점,...
k번째 문제는 k점으로 계산.
- 틀린 문제는 0점으로 계산
'''
import sys

n = int(input())
list = map(int, input().split())
score = 0
count_s = 0
for i in list:
    if i == 0:
        count_s = 0
        continue
    elif i == 1:
        score = score + count_s + 1
        count_s += 1

print(score)

# answer
import sys
sys.stdin=open("input.txt"), "r")
n=int(input())
a=list(map(int,input().split()))
sum = 0
cnt=0
for x in a:
  if x ==1:
    cnt += 1
    sum += cnt
   else:
    cnt=0
print(sum)
