'''
2023-05-03
정성욱
#문제정의
    1~입력받은 숫자까지의 합계 구하기
#문제분석
    변수-num1(정수1),합계(total)
#알고리즘
    1.변수선언
        num1에 정수 입력
        total=0
    2.논리(반복)
        (조건) for i in range(1,num1+1)
    3.합계 출력
'''

#for반복
num1 = int(input("입력받을 숫자를 입력: "))
total = 0 #합계

for i in range(1, num1 + 1) :
    total = total + i #합계 저장

print('1~{}까지의 합계는 {}'.format(num1,total)) #결과 출력

#while반복
num1 = int(input("입력받을 숫자를 입력: "))

i = 1 #반복 횟수 초기화
total = 0 #합계

while i <= num1 : #반복 조건
    total = total  + i #합계 저장
    i = i + 1 #i 1증가

print('1~{}까지의 합계는 {}'.format(num1,total)) #결과 출력