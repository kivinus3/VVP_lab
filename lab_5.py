from math import sqrt


def task_1(x1, y1, x2, y2):
    print("Расстояние: " + str((sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))))
    print()


def task_2(a, b, c):
    print("Длина AC: " + str(abs(c - a)))
    print("Длина BC: " + str(abs(c - b)))
    print()


def task_3(a, b, c):
    print("Произведение длин AC и BC: " + str(abs(c - a) * abs(b - c)))
    print()


def task_4(x1, y1, x2, y2):
    a = abs(x2 - x1)
    b = abs(y2 - y1)
    print("Периметр: " + str((a + b) * 2))
    print("Площадь: " + str(a * b))
    print()


def task_5(x1, y1, x2, y2, x3, y3):
    a = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    b = sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
    c = sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
    P = a + b + c
    p = P / 2
    print("Периметр: " + str(P))
    print("Площадь: " + str(sqrt(p * (p - a) * (p - b) * (p - c))))
    print()


def main():
    print("\n1.")
    task_1(float(input("Введите x1: ")), float(input("Введите x2: ")), float(input("Введите y1: ")),
           float(input("Введите y1: ")))
    print("\n2.")
    task_2(float(input("Введите A: ")), float(input("Введите B: ")), float(input("Введите C: ")))
    print("\n3.")
    task_3(float(input("Введите A: ")), float(input("Введите B: ")), float(input("Введите C: ")))
    print("\n4.")
    task_4(float(input("Введите x1: ")), float(input("Введите y1: ")), float(input("Введите x2: ")),
           float(input("Введите y2: ")))
    print("\n5.")
    task_5(float(input("Введите x1: ")), float(input("Введите y1: ")), float(input("Введите x2: ")),
           float(input("Введите y2: ")), float(input("Введите x3: ")), float(input("Введите y3: ")))


if __name__ == '__main__':
    main()
