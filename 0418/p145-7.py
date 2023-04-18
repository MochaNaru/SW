'''
2023-04-18
정성욱
p145 3장 연습문제 7번
두 정수 입력 x>y -> x//y, x<y -> x+y, x==y -> x*y
단, 나눗셈의 몫을 계산할때는 y는 0 안됨
#문제분석
    변수:x(정수1), y(정수2)
#알고리즘
    1.변수선언
        num1(x)와  num2(y)에 정수 입력 받기
    2.논리(선택.중첩if)
        if x>y : 
            if y!=0 :
                x//y
        elif x<y:
            x+y
        else:
            x*y
'''

num1=int(input("x의 값을 입력하세요. : "))
num2=int(input("y의 값을 입력하세요. : "))

if num1>num2 : 
    if num2!=0 :
        print("{} // {} = {}".format(num1,num2,num1//num2))
    else:
        print("y의 값이 0 입니다.")
elif num1<num2:
    print("{} + {} = {}".format(num1,num2,num1+num2))
else:
    print("{} + {} = {}".format(num1,num2,num1+num2))