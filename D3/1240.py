import sys
sys.stdin = open("input.txt_1240","r")
code = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3,
        '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    for str in arr:
        if '1' in str:
            idx = len(str) - 1  # 끝 인덱스
            while str[idx] == '0':  # [1] 마지막 1인 인덱스 찾기
                idx -= 1

            ans = []

            for i in range(idx - 55, idx + 1, 7):  # [2] 7개씩 암호 읽어오기
                ans.append(code[str[i:i + 7]])

            tmp = sum(ans[0:8:2]) * 3 + sum(ans[1:8:2])
            if tmp % 10 == 0:
                tmp = sum(ans)
            else:
                tmp = 0

    print(f'#{test_case} {tmp}')