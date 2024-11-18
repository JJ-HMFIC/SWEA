import sys
sys.stdin = open("../../Review/input_1225.txt", "r")

for test_case in range(1,11):
    N = int(input())
    arr = list(map(int,input().split()))
    cnt = 1
    while True:
        tmp = arr[0] - cnt
        if tmp <=0:
            del(arr[0])
            arr.append(0)
            break
        arr.pop(0)
        arr.append(tmp)
        cnt += 1
        if cnt > 5:
            cnt = 1

    print(f'#{test_case}',end=' ')
    for lst in arr:
        print(lst, end=' ')
    print()
