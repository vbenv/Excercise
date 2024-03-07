# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B
# , 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램
try:
    Score = float(input("시험 점수를 입력해주세요. : "))
    if Score > 100 or Score < 0:
        print("시험 점수를 다시 입력해주세요")
    elif Score >= 90:
        print("A")
    elif Score >= 80:
        print("B")
    elif Score >= 70:
        print("C")
    elif Score >= 60:
        print("D")
    else:
        print("F")
except ValueError:
    print(f'{ValueError} : 숫자를 입력해주세요.')

