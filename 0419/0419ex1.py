'''
2023-04-19
정성욱
성별,키,몸무게를 입력 받아서 BMI지수를 구하고 비만도 측정하기
#문제분석
    변수-성별(sex), 키(height), 몸무게(weight), 평균BMI(avg)
    수식
        (남) height * height * 22
        (여) height * height * 21
        (BMI) weight/avg*100
#알고리즘
    1. 변수선언
        sex, height(실수), weight(실수)를 입력 받는다.
    2. 논리( 내포된 선택)
        if 성별이 여자 :
            avg 계산
            if avg >= 120 :
                "비만 체중"
            elif 110 < avg < 119 :
                "과체중"
            else :
                "표준 체중"
        elif  성별이 남자 :
        else :
            "성별 잘못 입력"
'''

sex=input("성별 입력('M or m' 또는 ' F or f) : ") #성별 입력 받기
height=float(input("키 입력(cm) : "))/100 #키 실수로 입력
weight=float(input("몸무게 입력(kg) : ")) #몸무게 실수로 입력

if (sex=='M' or sex=='m') : #남자
    avg=height*height*22 #표준체중
    bmi=weight/avg*100 #BMI 지수
    if 110 <= bmi <= 119 :
        print("과체중")
    elif bmi >= 120 :
        print("비만 체중")
    else :
        print("표준 체중")
elif (sex=='F' or sex=='f') : #여자
    avg=height*height*21 #표준체중
    bmi=weight/avg*100 #BMI 지수
    if 110 <= bmi <= 119 :
        print("과체중")
    elif bmi >= 120 :
        print("비만 체중")
    else :
        print("표준 체중")
else :
    print("성별 입력이 잘못 되었습니다.")