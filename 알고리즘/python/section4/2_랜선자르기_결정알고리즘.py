#answer
#결정 알고리즘
#특징1) 찾고자 하는 답이 특정 범위 안에 있음

import sys
sys.stdin=open("input.txt", "r")

#mid 값으로 만들 수 있는 줄의 수를 출력하는 함수
def Count(len):
    cnt=0
    for x in Line:
        cnt+=(x//len)
    return cnt

k, n=map(int, input().split())
Line=[]
res=0
largest=0

#줄바꿈이 된 줄 길이들을 읽어들이기 위한 for문
for i in range(k):
    tmp=int(input())
    Line.append(tmp)
    #가장 긴 랜선의 길이를 범위 기준으로 함
    largest=max(largest, tmp)
lt=1
rt=largest
while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=n:
        res=mid
        lt=mid+1
    else:
        rt=mid-1
print(res)







