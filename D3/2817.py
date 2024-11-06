import sys

sys.stdin = open("input_2817.txt", "r")


#sm = 합, n = 처음부터 순찰
def dfs(n, sm):
    global ans
    if K < sm: # 더했는데 합이 더 크면 그만
        return
    if n == N: # 끝애 왔고
        if sm == K: # 합이 같으면
            ans += 1 # 경우의 수 추가
        return
    dfs(n + 1, sm + arr[n])  # 사용하는 경우
    dfs(n + 1, sm)  # 사용하지 않는 경우


T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    ans = 0
    dfs(0, 0)
    print(f'#{test_case} {ans}')
