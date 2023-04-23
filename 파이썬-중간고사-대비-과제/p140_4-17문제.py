'''
2023-04-23
정성욱
나이와 키를 입력받아 입장가능한 롤러코스터를 출력하는 프로그램

#문제분석
    1.변수 - age(나이), height(키)
    2.수식 - 
#알고리즘
    1.변수지정
    2.조건(if~else)
        if age >= 8 :
            height=int(input)
            if height >= 120 :
                고속 입장가능
            else :
                저속 입장가능
        else :
            입장할 수 없습니다.
'''

age=int(input("나이를 입력 해주세요 : "))

if age >= 8 :
    height=int(input("키(cm)를 입력 해주세요 : ")) #나이가 8세 이상일때만 실행
    if height >= 120 :
        print("고속 롤러코스터 입장 가능")
    else :
        print("저속 롤러코스터 입장 가능")
else :
    print("입장할 수 없습니다.")