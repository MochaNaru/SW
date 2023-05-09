'''
2023-05-09
정성욱
#문제정의
    1~100까지의 입력받은 숫자의 배수의 합계
#문제분석
    변수-정수(num),합계(sum),반복변수(i)
#알고리즘
    1.변수 초기화
        num변수에 정수 입력
        sum = 0
        i = 0
    2.논리(반복안에 선택 포함 - while,if)
        i += 1
        while i <= 100 :
        i가 num의 배수가 아니면
            continue
        sum += i
'''
num=int(input("배수 숫자 입력 : "))

sum = 0
i = 0

while i < 100 : #선택조건
    i += 1
    if i%num != 0 : #선택 조건(i가 num의ㅐ 배수가 아니면)
        continue #반복의 처음으로 이동
    sum += i #num의 배수만 더하기
    
print("1~100까지의 {}의 배수의 합 {} : ".format(num,sum))