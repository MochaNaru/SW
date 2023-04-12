'''
2023-04-12
정성욱
평점을 입력받아서 평점출력, 4.2이상이면 "해외연수"
#문제분석
    변수-평점(score)
알고리즘
    1.변수선언
        (평점-score)에 실수(float로 입력받기
    2.논리(선택)
        if score>=4.2 :
'''

score=float(input("Enter your score : ")) #평점 실수로 입력
print("당신의 평점은 : ",score) #내가 입력한 평점
if score>=4.2: #조건
    print("해외연수") #조건이 참일경우 실행