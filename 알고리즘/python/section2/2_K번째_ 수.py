# 정답
import sys
#sys.stdin=open("input.txt", "rt")

T=int(input())
for t in range(T):
    n, s, e, k=map(int, input().split())
    a=list(map(int, input().split()))
    a=a[s-1:e]
    a.sort()
    print("#%d %d" %(t+1, a[k-1]))

#my answer
import sys
sys.stdin = open("input.txt", "r")

t = int(input())
for i in range(1, t+1):
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split(" ")))
    b = []

    for z in range(s-1, e):
        b.append(a[z])
    b.sort()
    #TypeError: can only concatenate str (not "int") to str 
    #int -> str
    print("#"+str(i)+" "+str(b[k-1]))
