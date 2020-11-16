def main():
    sq_list = [i ** 2 for i in range(2, 1000)]
    sq_set = set(sq_list)
    for i, v1 in enumerate(sq_list):
        for v2 in sq_list[i + 1:]:
            if v1 + v2 in sq_set:
                a = v1 ** .5
                b = v2 ** .5
                c = (v1 + v2) ** .5
                diff = a + b + c - 1000
                if abs(diff) < .1:
                    print(f'a: {a}\nb: {b}\nc: {c}\n')
                    return a * b * c


print(main())
