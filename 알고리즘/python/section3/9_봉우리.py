#my answer
import sys

sys.stdin = open("input.txt", "r")

n = int(input())
listA = [list(map(int, input().split())) for _ in range(n)]

listA.insert(n, [0 for _ in range(n+2)]) #대신 append 사용 가능
listA.insert(0, [0 for _ in range(n+2)])

result = []

for i in range(1, n + 1):
    listA[i].insert(n, 0)
    listA[i].insert(0, 0)
    
    for z in range(1, n+1):
        if listA[z][i] > listA[z-1][i] and listA[z][i] > listA[z+1][i] and listA[z][i] > listA[z][i+1] and listA[z][i] > listA[z][i-1]:
            result.append(listA[z][i])
print(result)
print(len(result))
#=> 정답 9로 출력됨 왜 그런지 확인해보자

#answer
import sys
#sys.stdin = open("input.txt", 'r')
#행 
dx=[-1, 0, 1, 0]
#열
dy=[0, 1, 0, -1]
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
a.insert(0, [0]*n)
a.append([0]*n)
for x in a:
    x.insert(0, 0)
    x.append(0)

cnt=0
for i in range(1, n+1):
    for j in range(1, n+1):
        #a[i][j]>a[i+dx[k]][j+dy[k]] 가 모두 true인 것 
        #all 함수 => 인자로 넘어온 자료 구조 내의 모든 요소가 참일 때만 True를 반환

        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt+=1
print(cnt)
