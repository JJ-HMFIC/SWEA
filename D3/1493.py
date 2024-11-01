import sys

sys.stdin = open("input_1493.txt", "r")

L= 300
lst = [1] * L
for i in range(2, L):
    lst[i] = lst[i-1] + i - 1
# 첫 열 1,2,4,7,... 을 표현한 리스트
# 규칙은 1+2+3+... 순으로
def pos(n):
    si = 1
    while lst[si] <= n:
        si += 1
    si -= 1  # 값과 비교하여 계속 올라감, 올라간 후에 한칸 내림(한 칸 내려야 같은 대각선에 위치)
    # sy = 행 , 여기서는 층
    d = n - lst[si]  # 대각선의 첫 값과의 거리(비교)

    return si-d, d+1
    # y 좌표 : 대각선에서 증가할 수록 층이 하나씩 떨어짐 => 따라서 첫 층에서 차이만큼
    # 떨어지면 목표 y좌표
    # x 좌표 : 차이만큼 전진함 , 시작이 1 => d+1


T = int(input())
for test_case in range(1, T + 1):
    p, q = map(int, input().split())

    pi, pj = pos(p)
    qi, qj = pos(q)
    si, sj = pi + qi, pj + qj  # 목표 x,y좌표

    ans = lst[si+sj-1]+sj-1

    print(f'#{test_case} {ans}')

# https://www.youtube.com/watch?v=sujzigyPypY&t=1464s
# 너무 어렵다...