import sys
sys.stdin = open("input_1206.txt", "r")

T = 10
for test_case in range(1, T + 1):
    num = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(2, num - 2):
        tmp = arr[i-2:i+3]
        cmp = max(tmp[0],tmp[1],tmp[3],tmp[4])
        mid = tmp[2]

        if mid > cmp:
            cnt += mid - cmp

    print(f'#{test_case} {cnt}')
