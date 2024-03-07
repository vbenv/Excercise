# 두 정수 A,B가 주어졌을 때, A,B 비교하는 프로그램 작성

A,B = input("A와 B를 입력하세요: ").split()
A= int(A)
B = int(B)
if A <= -10000:
    print('A가 너무 낮습니다.')
elif B >= 10000:
    print('B가 너무 큽니다.')
elif A > B:
    print('>')
elif A <B:
    print('<')
else:
    print('==')

C,D = map(int, input("두 개 입력해봐라 ").split())

print(C,D)
print(type(C), type(D))
