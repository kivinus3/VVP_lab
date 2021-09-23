def task_1(a):
    print("\n1.")
    print("Количество полных килобайтов: " + str(a // 1024))
    print()


def task_2(a, b):
    print("\n2.")
    print("Количество отрезков В на отрезке А: " + str(a // b))
    print()


def task_3(a, b):
    print("\n3.")
    print("Незанятый остаток отрезка А: " + str(a % b))
    print()


def task_4(a):
    print("\n4.")
    print("Перестановка: " + str(a)[1] + str(a)[0])
    print()


def task_5(a):
    print("\n5.")
    print("Результат: " + str(a)[1] + str(a)[2] + str(a)[0])
    print()


def main():
    task_1(int(input()))
    task_2(float(input()), float(input()))
    task_3(float(input()), float(input()))
    task_4(int(input()))
    task_5(int(input()))


if __name__ == '__main__':
    main()