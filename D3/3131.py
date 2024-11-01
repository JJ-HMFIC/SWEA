def prime_num(n):
    is_prime = [True] * (n+1) # 기본값은 true
    is_prime[0] = is_prime[1] = False # 0과 1은 소수가 아님

    for i in range(2, int(n**0.5)+1):
        if is_prime[i]: #  i가 소수면
            for j in range(i*i,n+1,i):
                is_prime[j] = False # i의 배수는 소수가 아님

    primes = [num for num,prime in enumerate(is_prime) if prime] # 소수 배열

    return primes


primes = prime_num(1000000)
for i in primes:
    print(i, end=' ')

# 소수의 성질: 만약 어떤 수 n이 소수라면,
# n의 배수는 n보다 크거나 같은 수에서 시작합니다.
# 따라서 n의 제곱보다 큰 수들은 이미 n의 배수로 지워졌을 것입니다.

# 제곱근 사용: 그래서 n의 배수를 찾으려면,
# n이 루트(limit)까지의 수일 때만 해당합니다.
# 이 범위까지만 체크하면 그 이후의 수는 이미 처리되었기 때문입니다.
# 에라토스테네스의 체