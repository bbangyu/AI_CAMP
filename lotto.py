import random


def main():
    numbers = random.sample(range(1,46),6)

    numbers.sort()

    print('로또 번호:',numbers)


if __name__ == "__main__":
    main()