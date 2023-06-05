'''
2023-06-06
정성욱
#문제정의
    다음과 같은 리스트를 생성하고,회전 횟수를 입력받아 
    입력된 횟수만큼 회전된 리스트를 출력하는 프로그램작성
#문제분석
    변수-회전 횟수입력(rotation_count)
#알고리즘
'''

def rotate_list(lst, rotations):
    rotations = rotations % len(lst)  # 입력된 횟수를 리스트의 길이로 나눈 나머지로 정규화
    
    rotated_lst = lst[-rotations:] + lst[:-rotations]  # 리스트를 회전하여 새로운 리스트 생성
    
    return rotated_lst

# 최초의 리스트 생성
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 회전 횟수 입력 받기
rotation_count = int(input("회전 횟수를 입력하세요: "))

# 리스트 회전
rotated_list = rotate_list(original_list, rotation_count)

# 결과 출력
print(f"{rotation_count}회전된 리스트: {rotated_list}")
