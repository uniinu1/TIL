#answer
#이분검색은 맨 왼쪽 변수 lt, 맨 오른쪽 변수 rt, 중간 지점 변수 세 가지가 필요
#1024개를 10 번 안에 무조건 찾을 수 있음 왜냐면 경우의 수가 절반씩 계속 줄어드므로
import sys
sys.stdin=open("input.txt", "r")
n, m=map(int, input().split())
a=list(map(int, input().split()))
a.sort()

lt=0
rt=n-1
while lt<=rt:
    mid=(lt+rt)//2
    if a[mid]==m:
        print(mid+1)
        break
    elif a[mid]>m:
        rt=mid-1
    else:
        lt=mid+1
