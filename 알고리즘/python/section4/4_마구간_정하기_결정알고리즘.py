
#수직선 상에 정렬되어야 하므로 리스트로 받아서 오름차순해야함

import sys
sys.stdin=open("input.txt", "r")
def Count(len):
    cnt=1
    #첫 번째 마구간에 말 한 마리 배치하는 코드
    ep=Line[0]
    for i in range(1, n):
        if Line[i]-ep>=len:
            cnt+=1
            ep=Line[i]
    return cnt

n, c=map(int, input().split())
Line=[]

for _ in range(n):
    tmp=int(input())
    Line.append(tmp)
Line.sort()
lt=1
rt=Line[n-1]
while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=c:
        res=mid
        lt=mid+1
    else:
        rt=mid-1

print(res)


