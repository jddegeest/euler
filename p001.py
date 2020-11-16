def main():
    threes = set(range(3, 1000, 3))
    fives = set(range(5, 1000, 5))
    print(sum(threes | fives))


main()
