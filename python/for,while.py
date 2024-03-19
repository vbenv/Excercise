# def count_turns(M, N):
#     # 선이 꺾이는 횟수를 세는 함수
#     # M: 세로 줄 수, N: 가로 칸 수
#     # 현재 위치와 방향을 나타내는 변수들을 초기화합니다.
#     row, col = 0, 0  # 시작 위치는 표의 왼쪽 위
#     turns = 0  # 선이 꺾이는 횟수
    
#     # 달팽이 모양으로 선을 그리면서 꺾이는 횟수를 세는 반복문
#     while row < M and col < N:
#         # 오른쪽 방향으로 선을 그립니다.
#         for i in range(col, N):
#             turns += 1
#             col = i
#         row += 1
        
#         # 아래쪽 방향으로 선을 그립니다.
#         for i in range(row, M):
#             turns += 1
#             row = i
#         N -= 1
        
#         # 왼쪽 방향으로 선을 그립니다.
#         if row < M:
#             for i in range(N - 1, col - 1, -1):
#                 turns += 1
#                 col = i
#             M -= 1
        
#         # 위쪽 방향으로 선을 그립니다.
#         if col < N:
#             for i in range(M - 1, row - 1, -1):
#                 turns += 1
#                 row = i
#             col += 1
    
#     return turns - 1  # 시작점에서 선을 그리기 시작하므로 1을 빼줍니다.

# # 예시: 5줄 4칸 표에서 선이 꺾이는 횟수 계산
# M, N = map(int, input().split(" "))
# turns = count_turns(M, N)
# print(turns-1)

def print_star_pattern(rows):
    # 윗부분 출력
    for i in range(rows):
        print(" " * (rows - i - 1) + "*" * (2 * i + 1))
#     # 아랫부분 출력
#     for i in range(rows - 2, -1, -1):
#         print(" " * (rows - i - 1) + "*" * (2 * i + 1))

# # 예시: 5단계로 된 패턴 별찍기
rows = int(input())
print_star_pattern(rows)


# 2.
# def calculate_distance(num1, num2):
#     # 두 자연수 사이의 직각거리를 계산하는 함수
#     # 가로, 세로 방향으로 이동하는 거리를 계산합니다.
#     # 동서방향 거리 계산
#     horizontal_distance = abs((num1) % 4 - (num2) % 4)
#     # 남북방향 거리 계산
#     vertical_distance = abs((num1) // 4 - (num2) // 4)
    
#     # 직각거리는 가로방향 거리와 세로방향 거리의 합입니다.
#     return horizontal_distance + vertical_distance

# # 예시: 원숭이가 생각한 두 자연수 사이의 직각거리 계산
# num1, num2 = map(int, input().split(" "))
# distance = calculate_distance(num1, num2)
# print(distance)

# 1.
# def calculate_R2(R1, S):
#     # R2를 계산하는 함수
#     return (S * 2) - R1

# # 상근이가 기억하고 있는 R1과 S
# R1, S = map(int, input().split(" "))

# # R2 계산
# R2 = calculate_R2(R1, S)
# print(R2)

# R1, S = map(int, input().split(" "))
# R2 = (S*2 - R1)
# print(R2)


# def print_stars(arr):
#     for i in range(arr):
#         print(" " + )