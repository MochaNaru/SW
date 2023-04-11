'''
2023-04-11
정성욱
선택문-if~elif~else
성적이 90 이상이면 'A', 80 이상 90 미만이면 'B'
70 이상 80 미만이면 'C', 70 미만이면 'F'
'''

score=int(input("성적 입력:"))

if score>=90: #조건1
    print("A학점") #조건 1이 참인 경우
elif score>=80: #조건2
    print("B학점") #조건 2가 참인 경우
elif score>=70: #조건3
    print("C학점") #조건 3이 참인 경우
else:
    print("F학점") #조건 1,2,3 이 모두 거짓인 경우


