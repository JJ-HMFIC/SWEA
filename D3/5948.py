import sys

sys.stdin = open("input_5948.txt", "r")

T = int(input())
N = 7
for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    ans_set = set()
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if i != j and j != k and k != i:
                    ans_set.add(arr[i] + arr[j] + arr[k])

    result = sorted(ans_set)[-5]

    print(f'#{test_case} {result}')
# https://florescene.tistory.com/404
