import sys
sys.stdin = open("input_1228.txt","r")

T = 10
for test_case in range(1,T+1):
    N = int(input())
    data = list(input().split())
    num = int(input())
    command = [x.split() for x in input().split('I')[1:]]


    for i in command:
        start = int(i[0])
        many = int(i[1])
        to_insert = i[2:]

        data = data[:start] + to_insert + data[start:]

    print(f'#{test_case} {" ".join(data[:10])}')




#https://better21.tistory.com/48





