#answer
#lt : 1, rt : 45(분을 모두 합한 시간)
#이분검색으로 용량 줄여가면서 확인

import sys
sys.stdin=open("input.txt", "r")

def Count(capacity):
    cnt=1
    sum=0
    for x in Music:
        if sum+x>capacity:
            cnt+=1
            sum=x
        else:
            sum+=x
    return cnt

n, m=map(int, input().split())
Music=list(map(int, input().split()))


# 반례 위해서 집어넣음
# 노래들 중에서 가장 긴 노래를 담을 수 있는 용량은 가지고 있어야 함 
maxx=max(Music)
lt=1
rt=sum(Music)
res=0
while lt<=rt:
    mid=(lt+rt)//2
    if mid>=maxx and Count(mid)<=m:
        res=mid
        rt=mid-1
    else:
        lt=mid+1
print(res)

# 위의 코드는 반례가 있었음
"""
9 9 
1 2 3 4 5 6 7 8 9
가 입력이 되었을 때
"""
