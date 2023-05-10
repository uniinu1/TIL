#Me
#자연수 N 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램
#만약 20 입력되면 1부터 20까지의 소수는 2, 3, 5, 7, 11 ,13, 17, 19로 총 8개

import sys
#sys.stdin=open("in5.txt", "rt")

T = int(input())
result = 1
for t in range(3, T+1):
    i = 0
    if t % 2 == 0:
        continue
    for z in range(1, t):
        if z > 1 and t % z == 0:
            i += 1

    if i == 0:
        result += 1

print(result)

#시간 초과로 정답 맞추지 못함
#Answer
