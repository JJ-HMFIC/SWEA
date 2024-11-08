import sys

sys.stdin = open("input_1860.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())  # M 초에 K개의 붕어빵
    arr = list(map(int, input().split()))
    arr.sort()

    ans = 'Possible'
    cnt = 0  # 사람 수

    for i in arr:
        cnt += 1
        if (i // M) * K < cnt:
            ans = 'Impossible'
            break
    print(f'#{test_case} {ans}')
#https://www.youtube.com/watch?v=jFVUB7c38Q4