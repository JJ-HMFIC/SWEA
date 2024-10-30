import sys

sys.stdin = open("input_1209.txt", "r")

T = 10
for test_case in range(1, T + 1):
    N = 100
    num = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr2 = list(zip(*arr))
    result = 0
    trans1, trans2 = 0, 0
    for i in range(N):
        trans1 += arr[i][i]
        trans2 += arr[N - i - 1][N - i - 1]
    for lst1 in arr:
        tmp = sum(lst1)
        if result < tmp:
            result = tmp
    for lst1 in arr2:
        tmp = sum(lst1)
        if result < tmp:
            result = tmp

    if result < max(trans1, trans2):
        result = max(trans1, trans2)

    print(f'#{num} {result}')
