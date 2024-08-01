"""
https://www.acmicpc.net/problem/10871

<input>
첫째 줄에 테스트 케이스의 개수 T가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 
각 줄에 A와 B가 주어진다. (0 < A, B < 10)

<output>
각 테스트 케이스마다 "Case #x: "를 출력한 다음,
 A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.
"""
T = int(input()) # T 정수로 받기
i = 0 # 초기값 설정
print("") # 한 줄 띄어쓰기

while(i < T):
    A,B = map(int,input().split(' '))
    print("Case #", i+1, ": ", A+B)
    i += 1
	
    
		
