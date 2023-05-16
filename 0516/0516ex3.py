'''
2023-05-16
정성욱
파일 입출력 - 읽기(read() - 전체 내용을 하나의 문자열로 변환)
'''

f=open("C:/data/test.txt","r") #파일 객체 생성(읽기)

txts=f.read() #파일 전체 내용을 txts에 하나의 문자열로 변환

print(txts) #읽은 내용 출력 

f.close() #파일 종료