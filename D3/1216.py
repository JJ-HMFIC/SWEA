import sys
sys.stdin = open("input_1216.txt", "r")

T = 10
def is_pal(arr, leng):
    for lst in arr: # 행마다 조사
        for i in range(N-leng+1): #
            if lst[i:i+leng] == lst[i:i+leng][::-1]: # N개의 길이 부터 1까지 회문 검사
                return True # 회문 발견 = 회문의 길이
    return False
def is_pal_idx(arr,leng):
    for lst in arr:
        for i in range(N-leng+1):
            for j in range(leng//2):
                if lst[i+j] != lst[i+leng-1-j]:
                    break
                else:
                    return True
    return False
for test_case in range(1,T+1):
    num = int(input())
    N = 100
    arr = [input() for _ in range(N)]
    arr2 = [''.join(x) for x in zip(*arr)] # 전치

    for leng in range(N,1,-1):
        if is_pal_idx(arr, leng) or is_pal_idx(arr2, leng): # leng = 회문의 길이
            break

    print(f'#{num} {leng}')