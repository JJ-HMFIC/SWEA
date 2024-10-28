#1208. [S/W 문제해결 기본] 1일차 - Flatten
import sys
sys.stdin = open("input_1208.txt", "r")

T = 10
for test_case in range(1,T+1):
    dump = int(input())
    box = list(map(int, input().split()))

    while dump:
        max_box = max(box)
        min_box = min(box)

        max_idx = box.index(max_box)
        min_idx = box.index(min_box)

        box[max_idx] -= 1
        box[min_idx] += 1

        dump -= 1

    result = max(box) - min(box)

    print(f'#{test_case} {result}')