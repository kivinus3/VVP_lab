from math import sqrt


def task_1(x1, y1, x2, y2):
    print("\n1.")
    print("Расстояние: " + str((sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))))
    print()


def task_2(a, b, c):
    print("\n2.")
    print("Длина AC: " + str(abs(c - a)))
    print("Длина BC: " + str(abs(c - b)))
    print()


def task_3(a, b, c):
    print("\n3.")
    print("Произведение длин AC и BC: " + str(abs(c - a) * abs(b - c)))
    print()


def task_4(x1, y1, x2, y2):
    print("\n4.")
    a = abs(x2 - x1)
    b = abs(y2 - y1)
    print("Периметр: " + str((a + b) * 2))
    print("Площадь: " + str(a * b))
    print()


def task_5(x1, y1, x2, y2, x3, y3):
    print("\n5.")
    a = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    b = sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
    c = sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
    P = a+b+c
    p = P/2
    print("Периметр: " + str(P))
    print("Площадь: " + str(sqrt(p*(p-a)*(p-b)*(p-c))))
    print()


def main():
    task_1(int(input()), int(input()), int(input()), int(input()))
    task_2(int(input()), int(input()), int(input()))
    task_3(int(input()), int(input()), int(input()))
    task_4(int(input()), int(input()), int(input()), int(input()))
    task_5(int(input()), int(input()), int(input()), int(input()), int(input()), int(input()))


if __name__ == '__main__':
    main()
