'''
2023-06-13
정성욱
사용자 정의 모듈 호출
'''
import polyArea

w = float(input("사각형의 가로:"))
d = float(input("사각형의 세로:"))

print("사각형의 넓이:",polyArea.rectangleArea(w,d))