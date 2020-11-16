from commons import gen_prime


def prime_factorization(n):
    factors = []
    remainder = n
    for p in gen_prime(n / 3):
        if p > remainder:
            break
        if remainder % p == 0:
            exp = 1
            remainder = remainder / p
            while True:
                if remainder % p == 0:
                    exp += 1
                    remainder = remainder / p
                else:
                    factors.append([p, exp])
                    break
    return factors


def main():
    n = 600851475143
    print(prime_factorization(n)[-1][0])
    # print(prime_factorization(13195))


main()
