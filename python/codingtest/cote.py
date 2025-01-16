# 프로그래머스, 콜라츠 수열 만들기


def solution(x):
    answer = []
    while x > 1:
        answer.append(int(x))
        if (x % 2) == 0 :
           x = x / 2
        elif (x%2) == 1:
            x = 3 * x + 1
    answer.append(1)
    return answer

print(solution(10))