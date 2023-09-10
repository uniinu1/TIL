#내풀이
import sys
#sys.stdin = open("input.txt", "r")

n=int(input())
#2차원 배열로 받기
a=[list(map(int, input().split())) for _ in range(n)]

maxNum = 0
dae = 0
dae2 = 0
for x in range(n):
    hang = 0
    col = 0
    for y in range(n):
        hang = a[x][y] + hang
        col = a[y][x] + col
        if x == y:
            dae = dae + a[x][x]

        if x + y == n -1:
            dae2 = a[x][y] + dae2

    if hang > maxNum:
        maxNum = hang
        
    if col > maxNum:
        maxNum = col
        

if dae > maxNum:
    maxNum = dae

if dae2 > maxNum:
    maxNum = dae2
    
print(maxNum)

#정답
largest = -2147000000
for i in range(n):
    sum1 = sum2=0
    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]
    if sum1 > largest:
        largest=sum1
    if sum2 > largest:
        largest=sum2

sum1=sum2=0
for i in range(n):
    sum1 += [i][i]
    sum2 += [i][n-i-1]

if sum1 > largest:
    largest=sum1
if sum2 > largest:
    largest=sum2
