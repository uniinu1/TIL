# 그리디란 단계에서 가장 중요한 것을 선택하는 것
# 그리디는 정렬한 다음 차례 차례 선택하는 것으로 진행됨


import sys
sys.stdin=open("input.txt", "r")
n=int(input())
meeting=[]
for i in range(n):
    a, b=map(int, input().split())
    meeting.append((a, b))

#그냥 튜플로 sort하면 앞 key 값을 가지고 sort를 해줌
#meeting.sort()
# 아래와 같이 lambda써야 끝나는 시간으로 sort 해줌
meeting.sort(key=lambda x : (x[1], x[0]))
et=0
cnt=0
for x, y in meeting:
    if x>=et:
        et=y
        cnt+=1
print(cnt)
