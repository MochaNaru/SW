'''
2023-04-05
정성욱
본봉과 수당을 정수로 입력 받아서 이번달 월급 수령액 구하는 프로그램(p116-9)
'''


sal=int(input('본봉')) #본봉 입력
exp=int(input('수당')) #수당 입력

tax=(sal+exp)*0.2 #세금계산
total_sa1=sal+exp-tax #수령액 계산

print("본봉이{}이고, 수당이 {}일때 실수령액은{}이다.".format(sal,exp,total_sa1))

