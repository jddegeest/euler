from commons import gen_prime
N = 10001
# N = 6

def main():
    for i, p in enumerate(gen_prime(13**99)):
        if i < N - 1:
            if i % 100 == 0:
                print(f'{i + 1}: {p}')
        else:
            print(f'{i + 1}: {p}')
            break


main()
