'''
2023-05-24
정성욱
#문제정의
    248p-3
    score1.txt 파일을 읽어와서 각 학생의 등급을 결정하고
    결과를 report1.txt 파일에 저장하기
'''

score = [] #빈 리스트 변수 생성 
f=open("C:/data/socore1.txt","r") #읽기 객체 생성

for i in range(10) : #10명의 학생 점수 읽어 오기
    score.append(f.readline().split()) #한 줄씩 읽어서 공백을 기준으로 나누도 score 리스트에 추가

for j in range(10) : #10명의 점수에 대한 등급 계산
    score[j][1]=float(score[j][1]) #문자열을 실수로 변환

    if score[j][1] >= 90 : #점수가 90 이상이면
        score[j].append("A")
    elif score[j][1] >= 80 : #점수가 80~89이면
        score[j].append("B")
    elif score[j][1] >= 70 : #점수가 70~79이면
        score[j].append("C")
    else : #점수가 70미만이면
        score[j].append("D")
for i in range(10): #10명 등급 화면에 출력
    print("{:<5}{:>5}".format(score[i][0],score[i][2]))

f.close()