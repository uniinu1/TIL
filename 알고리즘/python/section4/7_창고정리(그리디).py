import math
import time
#창고 정리
# 처음 든 생각 : 배열에 넣고 max, min 함수 이용해서 하나씩 하나씩 돌면 풀 수는 있는데, 조정 횟수에 따라 시간이 많이 걸릴 수 있겠다
start = time.time()
math.factorial(100000)
end = time.time()
'''
import sys
sys.stdin=open("D:\강의\파이썬 알고리즘 문제풀이(코딩테스트 대비)\code\section4\input_6.txt", "r")
L=int(input())
a=list(map(int, input().split()))
m=int(input())
a.sort()
for _ in range(m):
    a[0]+=1
    a[L-1]-=1
    a.sort()

print(a[L-1]-a[0])

'''
#max, min과 sort방식 시간 비교해보기

#my answer
import sys
sys.stdin = open("D:\강의\파이썬 알고리즘 문제풀이(코딩테스트 대비)\code\section4\input_6.txt", "r")
n = int(input())
height = list(map(int, input().split()))
qn = int(input())


for a in range(qn):
    maxA = max(height)
    minB = min(height)
    maxIndex = height.index(maxA)
    minIndex = height.index(minB)
    height[maxIndex] = height[maxIndex] - 1
    height[minIndex] = height[minIndex] + 1

print(max(height) - min(height))

print(f"{end - start:.5f} sec")
