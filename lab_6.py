from math import sqrt


def task_1(a, b):
    print("\n1.")
    a, b = b, a
    print("a = " + str(a))
    print("b = " + str(b))
    print()


def task_2(a, b, c):
    print("\n2.")
    c, b, a = b, a, c
    print("a = " + str(a))
    print("b = " + str(b))
    print("c = " + str(c))
    print()


def task_3(a, b, c):
    print("\n3.")
    a, c, b = b, a, c
    print("a = " + str(a))
    print("b = " + str(b))
    print("c = " + str(c))
    print()


def task_4(x):
    print("\n4.")
    y = (3 * x ** 6) - (6 * x ** 2) - 7
    print("y = " + str(y))
    print()


def task_5(x):
    print("\n5.")
    y = (4 * (x - 3) ** 6) - (7 * (x - 3) ** 3) + 2
    print("y = " + str(y))
    print()


def task_6(a):
    print("\n6.")
    helper = a * a
    helper *= helper
    a = helper * helper
    print("Ответ: " + str(a))
    print()


def task_7(a):
    print("\n7.")
    helper1 = a * a
    helper2 = helper1 * a
    helper1 *= helper2
    helper2 = helper1 * helper1
    helper1 *= helper2
    print("Ответ: " + str(helper1))
    print()


def main():
    task_1(int(input()), int(input()))
    task_2(int(input()), int(input()), int(input()))
    task_3(int(input()), int(input()), int(input()))
    task_4(int(input()))
    task_5(int(input()))
    task_6(int(input()))
    task_7(int(input()))


if __name__ == '__main__':
    main()
