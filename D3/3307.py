import sys
sys.stdin = open("input_3307.txt", "r")

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    dp = [0]*N
    dp[0] = 1

    for i in range(1,N):
        for j in range(i-1,-1,-1):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i],dp[j]) # 뒤에 있는 애들보다 내가 더 크다면 걔네들을 포함
        dp[i] += 1 # 나를 포함해야 하니까 + 1

    print(f'#{test_case} {max(dp)}')