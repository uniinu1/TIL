#my answer
import sys
sys.stdin = open("input.txt", "r")

gamNum = int(input())
gam = [list(map(int, input().split())) for _ in range(gamNum)]

qNum = int(input())
q = [list(map(int, input().split())) for _ in range(qNum)]


for i in range(qNum):
    tempIdx = 999
    tempList = []
    s, d, n = q[i][0], q[i][1], q[i][2]
    # 5개 배열이면 5번 돌았을때 제자리임. 해당 조건 먼저 확인하여 쓸데없는 반복 돌지 않도록 하자
    if n % gamNum == 0:
       break; 
    #왼쪽, 오른쪽 분기문
    if(d == 0):
        for idx, val in enumerate(gam[s-1]):
            tempIdx = idx - n
            if tempIdx <0:
                # tempIdx 결과가 마이너스일 경우 +가 될 때까지 gamNum 더해줘야 인덱스번호가 됨
                while tempIdx < 0:
                    tempIdx += gamNum
            #IndexError: list assignment index out of range 오류
            #빈 배열에 이렇게 넣으면 오류나나,,?
            #tempList[tempIdx] = val
            tempList.insert(tempIdx, val)
    else:
        for idx, val in enumerate(gam[s-1]):
            tempIdx = idx + n   
            if tempIdx >= gamNum:
                while tempIdx > gamNum:
                    # tempIdx 결과가 gamNum보다 클 경우 
                    tempIdx -= gamNum
            tempList.insert(tempIdx, val)
    gam[s-1] = tempList


m = gamNum // 2
s = 0
e = gamNum
result=0

for a in range(gamNum):
    for t in range(s, e):

        result += gam[a][t]

    if a < m:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(gam)
print(result)
# 다른 답 출력 됨

#answer
#왼쪽 회전 : pop과 append로 간단하게 구현
#오른쪽 회전 : pop과 insert 이용
import sys
sys.stdin = open("input.txt", 'r')
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
m=int(input())
for i in range(m):
    h, t, k=map(int, input().split())
    if(t==0):
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))
    else:
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop())

res=0
s=0
e=n-1
for i in range(n):
    for j in range(s, e+1):
        res+=a[i][j]
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
print(res)
