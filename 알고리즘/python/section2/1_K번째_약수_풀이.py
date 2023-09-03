# my answer

#k번째 약수 
import sys 
#sys.stdin = open("input.txt", "r")

a = list(map(int, input().split(" ")))
b = []

for i in range(1, a[0] + 1):
    if a[0] % i == 0:
        b.append(i)
        if(a[1] - 1 == b.index(i)):
            print(b[a[1] -1])
            break
else:
    print(-1)

