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
    if n < e:
        for z in range(s):
            if(n == 1):
                result += a[e]
                s += 2
            elif(n != 1):
                a

# 결과 x

