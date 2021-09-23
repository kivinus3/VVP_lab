def task_1(n):
    print("\n1.")
    print("Секунд прошло с начала последней минуты: " + str(n % 60))
    print()


def task_2(k):
    print("\n2.")
    print("Номер дня недели: " + str((k % 7)))
    print()


def task_3(k, n):
    print("\n3.")
    print("Номер дня недели: " + str(((k + n - 2) % 7) + 1))
    print()


def task_4(a, b, c):
    print("\n4.")
    print("Уместилось квадратов: " + str((a * b) // (c ** 2)))
    print("Осталось места: " + str((a * b) % (c ** 2)))
    print()


def task_5(a):
    print("\n5.")
    print("Столетие: " + str((a - 1) // 100 + 1))
    print()


def main():
    task_1(float(input()))
    task_2(float(input()))
    task_3(float(input()), float(input()))
    task_4(float(input()), float(input()), float(input()))
    task_5(int(input()))


if __name__ == '__main__':
    main()
