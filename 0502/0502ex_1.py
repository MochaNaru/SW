'''
2023-05-02
정성욱
파이썬 내장 함수
'''

# 자료형 변환 함수
s='123114' # s 변수에 문자열 '123' 저장

ch1=int(s)  #ch1 변수에 s를 정수로 변환해서 저장
ch2=list(s) #ch2 변수에 s를 리스트로 변환해서 저장
ch3=tuple(s)    #ch3 변수에 s를 튜플로 변환해서 저장
ch4=set(s)  #ch4 변수에 s를 집합으로 변환해서 저장 (*중복제거)

print('{}의 자료형은 {}'.format(ch1, type(ch1)))
print('{}의 자료형은 {}'.format(ch2, type(ch2)))
print('{}의 자료형은 {}'.format(ch3, type(ch3)))
print('{}의 자료형은 {}'.format(ch4, type(ch4)))    # 순서가 없음

print() # 한줄 띄우기

num1=abs(-5)    #num1 변수에 -5의 절댓값 저장
num2=round(4.6) #num2 변수에 반올림 값 저장
num3=bin(10)    #num3 변수에 정수 10을 2진수로 변환해서 저장

str1=chr(97)    #str1 변수에 97에 해당하는 문자를 반환
str2=ord('A')   #str2 변수에 'A' 아스키 코드값 저장

print('-5의 절댓값 : ', num1)
print('4.6의 반올림값 : ', num2)
print('정수 10의 2진수값 : ', num3)
print('97에 해당하는 문자 : ', str1)
print('A의 아스키코드 값 : ', str2)

print() # 한줄 띄우기

num10={6,3,5,1,9,2,8}   #리스트 자료형
print('num10의 원소의 길이 : ', len(num10))
print('num10의 원소 중 가장 큰 값 : ', max(num10))
print('num10의 원소 중 가장 작은 값 : ', min(num10))
print('num10의 원소들의 합계 : ', sum(num10))
print('num10의 원소들 정렬 : ', sorted(num10))  #기본 오름차순 정렬

print() # 한줄 띄우기

print(zip('123',('kim','lee','park')))

#문자열과 튜플을 묶어서 리스트 자료형으로 반환
print(zip('123',('kim','lee','park')))
#문자열과 튜플을 묶어서 튜플 자료형으로 반환
print(list(zip('123',('kim','lee','park'))))

