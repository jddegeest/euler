def gen_fib():
    a, b = 1, 1
    yield 1
    while True:
        a, b = b, a + b
        yield b


def main():
    sum = 0
    for n in gen_fib():
        if n > 4000000:
            break
        if n % 2 == 0:
            sum += n
    print(sum)


main()
