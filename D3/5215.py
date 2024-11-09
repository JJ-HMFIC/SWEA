import sys

sys.stdin = open("input_5215.txt", "r")
def dfs(idx, taste, kcal):
    global max_taste
    if kcal > L:
        return
    if taste > max_taste:
        max_taste = taste
    if idx == N:
        return

    dfs(idx + 1, taste + t[idx], kcal + k[idx])
    dfs(idx + 1, taste, kcal)


T = int(input())

for test_case in range(1, T + 1):
    N, L = map(int, input().split())
    t = []
    k = []
    for i in range(N):
        a, b = map(int, input().split())
        t.append(a)
        k.append(b)

    max_taste = 0
    dfs(0, 0, 0)
    print(f'#{test_case} {max_taste}')
# https://velog.io/@seungjae/SWEA-5215-%ED%96%84%EB%B2%84%EA%B1%B0-%EB%8B%A4%EC%9D%B4%EC%96%B4%ED%8A%B8-Python-DFS