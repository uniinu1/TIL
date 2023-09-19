#my answer
#체크 따로 안 만들어도, 행/열/그룹의 합은 항상 1-9의 합과 같음 이런 식으로 구현해보자

#answer
#행 체크, 열 체크, 그룹체크 세 가지 필요
import sys
sys.stdin=open("input.txt", "r")
def check(a):
    for i in range(9):
        #행 체크
        ch1=[0]*10
        #열 체크
        ch2=[0]*10
        for j in range(9):
            ch1[a[i][j]]=1
            ch2[a[j][i]]=1
        if sum(ch1)!=9 or sum(ch2)!=9:
            return False
    #4중 for문으로 돌 수 밖에 없다 함
    #9개의 그룹확인
    for i in range(3):
        for j in range(3):
            ch3=[0]*10
            #9개의 숫자 확인
            for k in range(3):
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]]=1
            if sum(ch3)!=9:
                return False
    return True

a=[list(map(int, input().split())) for _ in range(9)]
if check(a):
    print("YES")
else:
    print("NO")
