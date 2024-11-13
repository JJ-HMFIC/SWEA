import sys

sys.stdin = open("input_1230.txt", "r")

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    data = list(input().split())
    num = int(input())
    command = list(input().split())

    for i in range(len(command)):
        if command[i] == 'I':
            tmp = command[i + 3:i + 3 + int(command[i + 2])]
            idx = int(command[i + 1])
            data = data[:idx] + tmp + data[idx:]
        elif command[i] == 'D':
            idx = int(command[i + 1])
            end = int(command[i + 2])
            data = data[:idx] + data[idx + end:]
        elif command[i] == 'A':
            num = int(command[i + 1])
            tmp = command[i + 2:i + 2 + num]
            data = data + tmp

    print(f'#{test_case} {" ".join(data[:10])}')
