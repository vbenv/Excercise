# 프로그래머스, 배열 만들기 4


def solution(arr):
    i = 0
    stk = []
    while i < len(arr):
        # stk is empty, append arr[i] to stk and add 1 to i
        if (len(stk) == 0):
            stk.append(arr[i])
            i += 1
        # last element in stk is smaller than arr[i], append arr[i] to stk
        elif stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
        else:
            stk.pop()
            
    return stk

print(solution([1,4,2,5,3]))