# 프로그래머스, 카운트 업


def solution(start_num, end_num):
    answer = []
    [answer.append(i) for i in range(start_num, end_num + 1)]
    return answer
print(solution(1,10))