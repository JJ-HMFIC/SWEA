import sys

sys.stdin = open("input_3282.txt", "r")



'''
def knapsack(W, wt, val, n):
    # 배낭의 무게 한도/ 각 아이템의 무게 / 각 아이템의 가치 / 아이템 수
    K = [[0 for _ in range(W+1)] for _ in range(n+1)]
    # 행은 아이템을 하나씩 담고(처음에 아무것도 담지 않음) / 열은 무게 한도(0부터 1씩 증가)
    # 배열의 데이터는 최대 가치
    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                K[i][w] = 0  # 0으로 세팅, 처음에 아무것도 안담으니까 or 무게 한도가 0이니까
            elif wt[i-1] <= w:
                # 현재 무게한도(w) 보다 현재 아이템의 무게(wt[i - 1])가 작다면
                # K[i-1][w - wt[i-1]] = i번째 아이템의 무게만큼 담고 나머지의 최대 가치(즉 i 번째를 담는다면)
                # + val[i-1] = i 번째 아이템의 가치
                # K[i-1][w] =  이전의 가치, 이게 더 크다면 담을 필요 없음
                K[i][w] = max(K[i-1][w - wt[i-1]] + val[i-1], K[i-1][w])
            else: # 현재 한도보다 무게가 크면 담지 않음
                K[i][w] = K[i-1][w]
    return K[n][W]
'''
T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())  # 무게한도 K, 아이템 수 N
    V = []  #부피 wt
    C = []  #가치 val
    dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
    for i in range(N):
        a, b = map(int, input().split())
        V.append(a)
        C.append(b)
    #result = knapsack(K, V, C, N)
    for i in range(1, N+1): # 아이템
        for j in range(1,K+1): # 무게
            if V[i-1] <= j:
                dp[i][j] = max(dp[i-1][j-V[i-1]]+C[i-1],dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    print(f'#{test_case} {dp[N][K]}')
# https://www.youtube.com/watch?v=rhda6lR5kyQ
# https://gsmesie692.tistory.com/113
