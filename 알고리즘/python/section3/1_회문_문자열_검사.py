# 회문 문자열 검사
# N개의 문자열을 입력받아 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우(== 회문 문자열)
# 회문 문자열이 맞으면 YES, 아니면 NO 출력
# 다만, 회문 검사할 때 대소문자 구분 X
# 입력 설명 : 첫 줄 정수 N이 주어지고, 다음 줄부터 N개의 단어가 입력된다. 각 단어의 길이는 100 넘지 않음
# 출력 설명 : 각 줄에 해당 문자열의 결과를 YES OR NO로 출력

# answer
import sys
sys.stdin = open("input.txt", "r")
n=int(input())

#방법1(방법2처럼 파이썬스러운 것도 좋지만 인터뷰 할 때 직접 짜라고 함. 이렇게 직
짜는 것 중요함)
for i in range(n):
    s=input()
    s=s.upper()
    size=s.len(s)
    #비교 횟수 == size//2
    for j in range(size//2):
        if s[j] != s[-1-j]:
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))

#방법2
for i in range(n):
    s=input()
    s=s.upper()
    # 문자열 reverse 시켜줌
    if s == s[::-1]:
        print("#%d YES", %(i+1))
    else:
        print("#%d NO" %(i+1))
