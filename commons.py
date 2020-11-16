def gen_prime(max_p):
    primes = [2]
    yield 2
    for n in range(3, int(max_p) + 1, 2):
        for p in primes:
            if n % p == 0:
                break
        else:
            primes.append(n)
            yield n


def list_prime(max_p):
    num_list = list(range(2, max_p + 1))
    num_set = set(num_list)
    i = 0
    while True:
        step = num_list[i]
        if step in num_set:
            stop = num_list[-1]
            mult_set = set(range(step * 2, stop, step))
            num_set -= mult_set
        i += 1
        if i == len(num_list) - 1:
            num_list = list(num_set)
            num_list.sort()
            return num_list
