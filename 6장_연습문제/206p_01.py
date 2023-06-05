'''
2023-06-06
정성욱
#문제정의
    입력된 문자가 회문인지는 판별하는 프로그램을 작성하시오
#문제분석
    변수-입력받는문자(input_string)
#알고리즘
'''

def is_palindrome(string):
    # 공백 제거 및 대소문자 통일
    string = string.replace(" ", "").lower()
    
    # 문자열을 뒤집어서 비교
    reversed_string = string[::-1]
    
    # 회문 여부 판별
    if string == reversed_string:
        return True
    else:
        return False

# 사용자로부터 문자열 입력 받기
input_string = input("문자열을 입력: ") 

# 회문 여부 판별
if is_palindrome(input_string):
    print("회문입니다.")
else:
    print("회문이 아닙니다.")
