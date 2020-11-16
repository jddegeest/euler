STR_LEN = 13


def update_max(str_loc, m):
    prod = 1
    for s in str_loc:
        prod *= int(s)
    return max(prod, m)


def main():
    with open('p8_inp.txt') as f:
        num_str = f.readline().strip()
    max_prod = 0
    total_len = len(num_str)
    for i in range(total_len - STR_LEN):
        max_prod = update_max(num_str[i: i + STR_LEN], max_prod)
    print(max_prod)


main()
