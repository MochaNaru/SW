'''
2023-04-11
정성욱
'''
num1=int(input("첫 번째 숫자 입력:"))
op=input("연산자(+,-,*,/)중 1개 입력:")
num2=int(input("두 번째 숫자 입력:"))

if op == "+": #조건1
    print (num1,op,num2,"=",num1+num2) #조건1 이가 참일 경우  
elif op == "-": #조건2
    print(num1,op,num2,"=",num1-num2) #조건2 이가 참일 경우
elif op == "*" : #조건3
    print(num1,op,num2,"=",num1*num2) #조건 3이가 참일 경우
else:
    print(num1,op,num2,"=",num1/num2) #조건 1,2,3 이가 다 거짓인 경우1

'''
if op == "+':
    print(num1,op,num2,"=",num1 + num2)
elif 
    print("{}{}{}={}".fomat(num1,op,num2,num1-num2))
elif 
    print("{}{}{}={}".fomat(num1,op,num2,num1*num2))
else 
    print("{}{}{}={}".fomat(num1,op,num2,num1/num2))
'''