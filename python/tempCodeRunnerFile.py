# mCn 구하는 공식
def mCn(M, N):
    m= 1
    n = 1
    mn = 1
    for i in range(2,M+1):
        m *= i
    for j in range(2,N+1):
        n *= j
    for k in range(2, M-N+1):
        mn *= k
    if M == N:
        return 1
    else:
        return int(m/((mn)*n))
N, M = map(int,input().split(" "))
print(mCn(M,N))