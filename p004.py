def get_values():
    values = set([i * j for i in range(100, 1000) for j in range(100, 1000)])
    values = list(values)
    values.sort(reverse=True)
    return values


def check_pal(value):
    str_val = str(value)
    str_len = len(str_val)
    str_len_mid = int(str_len / 2)
    if str_val[:str_len_mid] == str_val[str_len:str_len - str_len_mid - 1:-1]:
        return True
    else:
        return False


def main():
    all_values = get_values()
    for v in all_values:
        if check_pal(v):
            print(v)
            break


main()
