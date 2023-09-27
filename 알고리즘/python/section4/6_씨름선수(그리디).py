#씨름 선수 (그리디)

#우선은 키순으로 내림차순
#키가 제일 큰 사람은 무조건 선발
#두번째 사람은 나보다 큰 사람만 살펴보면 됨

#키와 몸무게를 같이 넣고 이중 for문 돌면 시간복잡도 높아지므로, 최대값 구하는 과정처럼 몸무게를 확인하자

'''
import sys
sys.stdin=open("input.txt", "r")

n=int(input())
body=[]

for i in range(n):
    a, b=map(int, input().split())
    body.append((a, b))

#키 기준으로 내림차순 정렬
body.sort(reverse=True)

largest=0
cnt=0
for x, y in body:
    if y>largest:
        largest=y
        cnt+=1
print(cnt)
'''

# my answer
import sys
sys.stdin=open("D:\강의\파이썬 알고리즘 문제풀이(코딩테스트 대비)\code\section4\input_6.txt", "r")
n=int(input())
people=[]
for i in range(n):
    a, b=map(int, input().split())
    people.append((a, b))

people.sort(reverse=True)
cnt = 1
bWeight = people[0][1]
people.pop(0)

for a in range(n - 1):
    if bWeight < people[a][1]:
        cnt += 1
        bWeight = people[a][1]
    
print(cnt)
