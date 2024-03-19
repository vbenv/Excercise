N = int(input())
if 1 <= N or N <= 9:
    for i in range(1,10):
        print(f"{N} * {i} =", i * N)