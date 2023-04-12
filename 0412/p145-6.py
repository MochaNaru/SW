'''
2023-04-12
정성욱
두숫자가 짝수면 합한결과를 입력
그렇지 않으면 몇번째 숫자를 짝수로 입력해야 하는지 출력
#문제분석
    변수 - 첫번째 정수-num1, 두번째 정수-num2 
    수식 - num1%2==0 / num2%2==0 / num1+num2
#알고리즘
    1.변수선언
        num1,num2에 정수 입력
    2.논리(선택 if~elif~else)
        if num1%2==0 and num2%2==0 :
            (두숫자가 참) num1,"+"num2=num1+num2
        elif num1%2==1 and num2%2==0 :
            (첫번째 숫자가 홀)"첫번째 정수를 짝수로 입력하세요."
        elif num1%2==0 and num2%2==1 :
            (두번째 숫자가 홀)"두번째 정수를 짝수로 입력하세요."
        else "
            (두숫자 모두 홀)"두 숫자 모두를 짝수로 입력하세요."
'''

num1=int(input("첫번째 정수를 입력 : "))
num2=int(input("두번째 정수를 입력 : "))

if num1%2==0 and num2%2==0 :
    print (num1,"+",num2,"=",num1+num2)
elif num1%2==1 and num2%2==0 :
    print ("첫번째 정수를 짝수로 입력하세요.")
elif num1%2==0 and num2%2==1 :
    print ("두번째 정수를 짝수로 입력하세요.")
else :
    print ("두 숫자 모두를 짝수로 입력하세요.")