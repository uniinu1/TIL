#정답
import sys

sys.stdin = open("input.txt", "r")

n = int(input())
ql = [list(map(int, input().split())) for _ in range(n)]

result = 0
s = n // 2
e = n // 2

for i in range(n):
    for b in range(s, e+1):
        print("i : "+str(i)+ " b : "+str(b))
        print(ql[i][b])
        result += ql[i][b]

    if i < n // 2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1

#my answer
import sys
sys.stdin = open("input.txt", "r")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

result = 0
s = 1
e = n // 2

for i in range(n):
    if i < e:
        for z in range(s):
            if(n == 1):
                result += a[e]
                # 간격을 2만큼 늘리기 위함
                s += 2
            elif(n != 1):
                a

# 결과 x

#my answer 2
import sys
sys.stdid = open("input.txt", "rt")

n = int(input())
listGam = [list(map(int, input().split())) for i in range(n)]
qn = int(input())
exit()

for i in range(qn):
    s, d, num = map(int, input().split())
    if d == 0:
        #왼쪽으로 돌 때
        for a in range(num):
            listGam[s-1].append(listGam[s - 1].pop(0))
    else:
        #오른쪽으로 돌 때
        for a in range(num):
            listGam[s-1].insert(0, listGam[s - 1].pop())

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
=> 안 돌아감,,,

