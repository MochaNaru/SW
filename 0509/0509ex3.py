'''
2023-05-09
정성욱
#문제정의
    입력받은 숫자의 팩토리얼 값 계산하기
#문제분석
    변수-정수(num),팩토리얼(fac)
#알고리즘
    1.변수 초기화
        num은 정수 입력
        fac = 1
    2.논리(반복 - for)
        for i in range(num, 0, -1) 
'''
num = int(input("팩토리얼 숫자 입력:"))
fac = 1

for i in range(num, 0, -1) : #반복 조건
    fac *= i # 팩토리얼 계산

print("%d의 팩토리얼 값은: " %num,fac)