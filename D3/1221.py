import sys
sys.stdin = open("input_1221.txt", "r")

word = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T = int(input())
for test_case in range(1, T + 1):
    case, num = input().split()
    arr = list(input().split())

    result = {key: arr.count(key) for key in word}

    print(case)
    for i in result:
        print(f'{i} ' * result[i], end=' ')
    print()
