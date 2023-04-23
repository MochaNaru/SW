'''
2023-04-23
정성욱
직급과 나이를 입력받아 연금대상자를 출력하는 프로그램

#문제분석
    1.변수 - level(직급), age(나이)
    level == 5 ~ 8, 40 or 50 <= age <= 49 or 59
#알고리즘
    1.변수선언 - 
    2.논리(if~else)
        if ((level == 7) or (level == 8)) and ((40 <= age) and (age <= 49)) :
            연금 80% 대상자입니다.
        elif ((level == 5) or (level == 6)) and ((50 <= age) and (age <= 59)) :
            연금 100% 대상자입니다.
        else :
            연급 대상자가 아닙니다.
'''

level = int(input("직급 입력 :"))
age = int(input("나이 입력 :"))

if ((level == 7) or (level == 8)) and ((40 <= age) and (age <= 49)) :
            print ("연금 80% 대상자입니다.")

elif ((level == 5) or (level == 6)) and ((50 <= age) and (age <= 59)) :
    print ("연금 100% 대상자입니다.")

else :
    print ("연급 대상자가 아닙니다.")