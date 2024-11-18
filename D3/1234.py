import sys
sys.stdin =open("../../Review/input_1234.txt", "r")

T = 10
for test_case in range(1,T+1):
    length, password = input().split()

    stack=[]
    for c in password:
        if stack and stack[-1]==c:
            stack.pop()
        else:
            stack.append(c)

    result = ''.join(stack)
    print(f'#{test_case} {result}')


