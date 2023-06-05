'''
2023-06-06
정성욱
#문제분석
    실행 결과를 참조하여 학생들의 답안을 채점하는 파이썬 프로그램을 작성하시오.
    5명의 학생들이 제출한 답안지의 답을 아래와 같이 내포된 리스트(2차원)를 생성한 뒤,
    문제의 정답을 프로그램에서 입력받아 학생들의 점수를 출력하시오.
#문제정의
    변수-정답입력(correct_answers)
#알고리즘
'''

def score_students(answers, correct_answers):
    scores = []
    
    for i in range(len(answers)):
        score = sum([1 for j in range(len(answers[i])) if answers[i][j] == correct_answers[j]])
        scores.append(score)
    
    return scores

# 정답 입력 받기
correct_answers = []
for i in range(1, 11):
    answer = int(input(f"{i}번: "))  # 정답을 정수로 입력받음
    correct_answers.append(answer)

# 학생들의 답안
students_answers = [
    [1, 3, 2, 4, 3, 1, 4, 2, 2, 1],
    [3, 2, 4, 2, 2, 1, 1, 3, 4, 1],
    [2, 4, 3, 2, 1, 2, 1, 3, 3, 4],
    [2, 3, 3, 1, 1, 3, 2, 2, 4, 4],
    [3, 1, 1, 2, 4, 1, 2, 3, 1, 3]
]

# 학생들의 점수 계산
scores = score_students(students_answers, correct_answers)

# 결과 출력
for i, score in enumerate(scores):
    print(f"학생 {i+1}의 점수: {score}점")
