# 문자와 숫자가 섞여있는 문자열이 주어지면 그 중 숫자만 추출하여 그 순서대로 자연수 만듦
# 만들어진 자연수와 그 자연수의 약수 개수 출력
'''
만약 “t0e0a1c2h0er”에서 숫자만 추출하면 0, 0, 1, 2, 0이고 이것을 자연수를 만들면 120이 
됩니다. 즉 첫 자리 0은 자연수화 할 때 무시합니다. 출력은 120를 출력하고, 다음 줄에 120
의 약수의 개수를 출력하면 됩니다.
추출하여 만들어지는 자연수는 100,000,000을 넘지 않습니다.

▣ 입력설명
첫 줄에 숫자가 섞인 문자열이 주어집니다. 문자열의 길이는 50을 넘지 않습니다.

▣ 출력설명
첫 줄에 자연수를 출력하고, 두 번째 줄에 약수의 개수를 출력합니다.

▣ 입력예제 1 
g0en2Ts8eSoft

▣ 출력예제 1
28
6
'''
# my answer
import sys
sys.stdin = open("input.txt","r")

string = input()
int_st = ''
for s in string:
  #php에서는 === 아니면 형식까지 맞추지 않아도 되는데, 파이썬은 형식까지 맞아야 하나봄
    if s == '0' or s == '1' or s == '2' or s == '3' or s == '4' or s == '5' or s == '6' or s == '7' or s == '8' or s == '9':
        int_st = int_st + s
    
int_st = int(int_st)
print(int_st)

cnt = 0
for i in range(2, int_st+1):
    if int_st % i == 0:
        cnt += 1
        print(i)

print(cnt)

# 약수 개수가 안 맞음,,(약수는 1 포함시켜야 하는데 제외시켜버려서!)

# answer
import sys
sys.stdin = open("input.txt","r")

s=input()
res=0
for x in s:
    if x.isdecimal():
        # 문자열을 int 숫자로 만들 수 있는 방
        res=res*10+int(x)
cnt=0
print(res)
for i in rage(1, res +1):
    if res %i == 0:
        cnt+=1
print(cnt)
