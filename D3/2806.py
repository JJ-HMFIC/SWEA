import sys

sys.stdin = open("input_2806.txt", "r")


def promising(x):
    for i in range(x):  # 인덱스 = 행 , row[n] 의 값 = 열
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:  # 열이 같거나 대각선 상에 놓여 있으면
            # abs(row[x] - row[i]) == x - i , 좌: 열의 차이 절대값, 우: 행의 차이 절대값(둘이 같으면 같은 대각선상)
            # for문을 보면 x는 i보다 큼 그래서 절대값 꼭 씌워주지 않아도 됌
            return False  # 못놔요
    return True


def dfs(x):
    global result

    if x == N:  # N개의 퀸을 다 놓으면
        result += 1  # 경우의 수 한 개 추가
    else:  # 각 행에 퀸 놓기
        for i in range(N):
            row[x] = i  # N번째 퀸 놓기
            if promising(x):  # 겹치는지 확인
                dfs(x + 1)  # 문제 없으면 다음


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    result = 0
    row = [0] * N

    dfs(0)

    print(f'#{test_case} {result}')
# row = [1, 3, 0, 2]의 예시 -> 0행의 1열, 1행의 3열에 퀸이 존재
# https://cheon2308.tistory.com/entry/SWEA-2806%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC-N-Queen
