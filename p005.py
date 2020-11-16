def main():
    check_list = [19, 18, 17, 16, 15, 14, 13, 12, 11]
    for i in range(20 * 19, 670442572800, 20):
        for n in check_list:
            if i % n > 0:
                break
        else:
            print(i)
            break


main()
