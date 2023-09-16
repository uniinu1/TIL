#정답
import sys
sys.stdin = open("input.txt", "r")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n) ]
res=0
s=e=n//2
for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1

print(res)

#my answer
import sys
sys.stdin = open("input.txt", "r")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

result = 0
s = 1
e = n // 2

for i in range(n):
    if n < e:
        for z in range(s):
            if(n == 1):
                result += a[e]
                s += 2
            elif(n != 1):
                a

2 5 // 2
1 2 3
0 1 2 3 4

