def task_1(a, b):
    a, b = b, a
    print("a = " + str(a))
    print("b = " + str(b))
    print()


def task_2(a, b, c):
    c, b, a = b, a, c
    print("a = " + str(a))
    print("b = " + str(b))
    print("c = " + str(c))
    print()


def task_3(a, b, c):
    a, c, b = b, a, c
    print("a = " + str(a))
    print("b = " + str(b))
    print("c = " + str(c))
    print()


def task_4(x):
    y = (3 * x ** 6) - (6 * x ** 2) - 7
    print("y = " + str(y))
    print()


def task_5(x):
    y = (4 * (x - 3) ** 6) - (7 * (x - 3) ** 3) + 2
    print("y = " + str(y))
    print()


def task_6(a):
    helper = a * a
    helper *= helper
    a = helper * helper
    print("Ответ: " + str(a))
    print()


def task_7(a):
    helper1 = a * a
    helper2 = helper1 * a
    helper1 *= helper2
    helper2 = helper1 * helper1
    helper1 *= helper2
    print("Ответ: " + str(helper1))
    print()


def main():
    print("\n1.")
    task_1(float(input("Введите a: ")), float(input("Введите b: ")))
    print("\n2.")
    task_2(float(input("Введите a: ")), float(input("Введите b: ")), float(input("Введите c: ")))
    print("\n3.")
    task_3(float(input("Введите a: ")), float(input("Введите b: ")), float(input("Введите c: ")))
    print("\n4.")
    task_4(float(input("Введите x: ")))
    print("\n5.")
    task_5(float(input("Введите x: ")))
    print("\n6.")
    task_6(float(input("Введите A: ")))
    print("\n7.")
    task_7(float(input("Введите A: ")))


if __name__ == '__main__':
    main()
