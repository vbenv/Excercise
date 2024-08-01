# 칸의 갯수 N 개를 입력받는다. 여기서 줄은 N-1
N = int(input())
line =[]
for i in range(N-1):
    line.append(list[map(int,input().split())])
W = int(input())

for i in range(N-1):
    print(line[i])
print("N:", N, "W:", W)
