from commons import list_prime


def main():
    p_list = list_prime(2000000)
    print(sum(p_list))

main()