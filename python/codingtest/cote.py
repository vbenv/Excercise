# 프로그래머스, 배열 만들기2(python)

def solution(l, r):
    result = []
    for i in range(l, r+1):
        check = True
        for s in str(i):
            if s != "5" and s != "0":
                check = False
                break
        if check == True:
            result.append(i)        
    if len(result) == 0:
        return [-1]
    return result

print(solution(1, 1000))
