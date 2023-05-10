#ME
# N개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 수를 출력하는 프로그램을 작성
# 예를 들어 32를 뒤집으면 23, 23은 소수니 출력
# 단 910 뒤집으면 19로 숫자화(첫 자리부터 연속된 0 무시)
# 뒤집는 함수인 def reverse(x) 와 소수인지를 확인하는 함수 def isPrime(x)를 반드시 작성

import sys
#sys.stdin=open("in2.txt", "r")

c = int(input())
list1 = list(map(int, input().split()))
list2 = []

def reverse(x):
    list_ori = list(str(x))
    list_ori.reverse()
    result = int("".join(list_ori))
        
    return result

def isPrime(x):
    global result
    if x % 2 == 0 and x != 2:
        result = False
    else:
        if x == 2:
            result = True
        elif x == 1:
            result = False
        else:
            for n in range(3, x):
                if x % n == 0:
                    result = False
                    break
                else:
                    result = True
                
    return result

for i in range(c):
    a = reverse(list1[i])
    list2.append(a)

for i in list2:
    if isPrime(i):
        print(i, end = " ")
    

#answer
import sys
sys.stdin=open("input.txt", "r")
n=int(input())
a=list(map(int, input().split()))

def reverse(x):
    res=0
    while x>0:
        t=x%10
        res=res*10 +t
        x=x//10
        
    return res

def isPrime(x):
    if x==1:
        return False
    # 약수는 1과 자기 자신 빼고 자신의 수에서 절반의 수에서만 약수가 존재
    # 2가 이 문법에서 소수가 들어간다는 게 믿기지 
    for i in range(2, x//2+1):
       if x%i==0:
           return False
    else:
        return True

for x in a:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end = ' ')















