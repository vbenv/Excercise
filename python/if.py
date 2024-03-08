
H,M = map(int, input("설정한 알람 시간을 입력해 주세요 : ").split(':'))

M = M - 45
if M < 0:
    M = (-M)
    H -= 1
    if H < 0:
        H = (-H)
    print("바뀐 알람 시간은 ", H, ":", M, " 입니다.")
else:
    print("바뀐 알람 시간은 ", H, ":", M, " 입니다.")