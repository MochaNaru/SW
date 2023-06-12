import math

result_list = []  # 결과값을 저장할 리스트

while True:
    print("\n사용 가능한 연산:")
    print("1. 공학용 계산기")
    print("2. 야드 파운드 계산기")
    print("3. 종료")

    cal=input("원하는 계산기의 종류를 입력하시오. :")

    if cal == '3':
        print("계산기를 종료합니다.")
        break

    if cal not in ['1', '2', '3']:
        print("올바른 선택지를 입력하세요.")
        continue

    if cal == '1':
        print("공학용 계산기를 실행합니다.")

        while True:
            print("\n사용 가능한 연산:")
            print("1. 덧셈")
            print("2. 뺄셈")
            print("3. 곱셈")
            print("4. 나눗셈")
            print("5. 거듭제곱")
            print("6. 제곱근")
            print("7. 삼각함수 (사인, 코사인, 탄젠트)")
            print("8. 로그 함수")
            print("9. 종료")

            choice = input("원하는 연산을 선택하세요 (1-9): ")

            if choice == '9':
                print("계산기를 종료합니다.")
                break

            if choice not in ['1', '2', '3', '4', '5', '6', '7', '8']:
                print("올바른 선택지를 입력하세요.")
                continue

            num1 = float(input("첫 번째 숫자를 입력하세요: "))

            if choice != '6':
                num2 = float(input("두 번째 숫자를 입력하세요: "))

            if choice == '1':
                result = num1 + num2
                print("덧셈 결과:", result)
            elif choice == '2':
                result = num1 - num2
                print("뺄셈 결과:", result)
            elif choice == '3':
                result = num1 * num2
                print("곱셈 결과:", result)
            elif choice == '4':
                if num2 != 0:
                    result = num1 / num2
                    print("나눗셈 결과:", result)
                else:
                    print("0으로 나눌 수 없습니다.")
            elif choice == '5':
                result = num1 ** num2
                print("거듭제곱 결과:", result)
            elif choice == '6':
                result = math.sqrt(num1)
                print("제곱근 결과:", result)
            elif choice == '7':
                angle = math.radians(num1)
                print("사인:", math.sin(angle))
                print("코사인:", math.cos(angle))
                print("탄젠트:", math.tan(angle))
            elif choice == '8':
                result = math.log10(num1)
                print("로그 함수 결과:", result)

            result_list.append(result)  # 결과값을 리스트에 추가

    elif cal == '2' :
        print("숫자를 야드, 파운드, 인치, 피트로 변환하는 계산기를 실행합니다.")

        while True:
            print("\n사용 가능한 변환:")
            print("1. (미터)m → (야드)yd")
            print("2. (킬로그램)kg → (파운드)lb")
            print("3. (미터)m → (인치)inch")
            print("4. (미터)m → (피트)ft")
            print("5. 종료")

            choice = input("원하는 변환을 선택하세요 (1-5): ")

            if choice == '5':
                print("계산기를 종료합니다.")
                break

            if choice not in ['1', '2', '3', '4']:
                print("올바른 선택지를 입력하세요.")
                continue

            value = float(input("변환할 값을 입력하세요: "))

            if choice == '1':
                yard = value * 1.0936
                print(f"{value} (미터)m 는 {yard} (야드)yd 입니다.")
            elif choice == '2':
                pound = value * 2.2046
                print(f"{value} (킬로그램)kg 은 {pound} (파운드)lb 입니다.")
            elif choice == '3':
                inch = value * 39.3701
                print(f"{value}  (미터)m 는 {inch} (인치)inch 입니다.")
            elif choice == '4':
                feet = value * 3.2808
                print(f"{value} (미터)m 는 {feet} (피트)ft 입니다.")

            result_list.append(value)  # 결과값을 리스트에 추가

    else:
        print("-Error- 처음부터 다시 입력해주세요.")

# 결과값을 파일로 저장
with open("result.txt", "w") as file: #파일을 쓰기모드로 열기
    for result in result_list:
        file.write(str(result) + "\n")

# 파일에서 결과값을 읽어와 리스트로 보관
with open("result.txt", "r") as file: #파일을 읽기모드로 열기
    stored_results = file.readlines()
    stored_results = [float(result.strip()) for result in stored_results]

print("저장된 결과값:", stored_results)