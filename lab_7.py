from math import pi


def task_1(a):
    print("\n1.")
    print(str(a / 180) + " π рад.")
    print()


def task_2(a):
    print("\n2.")
    print(str(a / pi) + " градусов")
    print()


def task_3(x, a, y):
    print("\n3.")
    print("цена за 1 кг " + str(a / x))
    print("цена за " + str(y) + " кг " + str(a / x * y))
    print()


def task_4(v1, v2, s, t):
    print("\n4.")
    print("Через " + str(t) + "ч расстояние будет " + str((v1 + v2) * t + s))
    print()


def task_5(a, b):
    print("\n5.")
    print(str(a) + "·x + (" + str(b) + ") = 0")
    print("x = " + str((-b) / a))
    print()


def task_6(a1, b1, c1, a2, b2, c2):
    print("\n6.")
    d = a1 * b2 - b1 * a2
    d1 = c1 * b2 - c2 * b1
    d2 = a1 * c2 - a2 * c1
    if d == 0:
        if d1 == 0 and d2 == 0:
            print("Бесконечное множество решений")
            return
        else:
            print("Нет решений")
            return
    print("x = " + str(d1 / d))
    print("y = " + str(d2 / d))
    print()


def main():
    task_1(float(input()))
    task_2(float(input()))
    task_3(float(input()), float(input()), float(input()))
    task_4(float(input()), float(input()), float(input()), float(input()))
    task_5(float(input()), float(input()))
    task_6(float(input()), float(input()), float(input()), float(input()), float(input()), float(input()))


if __name__ == '__main__':
    main()
