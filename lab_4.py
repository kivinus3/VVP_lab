def task_1(a, b):
    print("Площадь: " + str(a * b))
    print("Периметр: " + str((a + b) * 2))
    print()


def task_2(d):
    print("Длина: " + str(3.14 * d))
    print()


def task_3(a, b):
    print("Среднее арифметическое: " + str((a + b) / 2))
    print()


def task_4(a, b):
    sqrA = a * a
    sqrB = b * b
    print("Сумма: " + str(sqrA + sqrB))
    print("Разность: " + str(sqrA - sqrB))
    print("Произведение: " + str(sqrA * sqrB))
    print("Частное: " + str(sqrA / sqrB))
    print()


def task_5(a, b):
    normA = abs(a)
    normB = abs(b)
    print("Сумма: " + str(normA + normB))
    print("Разность: " + str(normA - normB))
    print("Произведение: " + str(normA * normB))
    print("Частное: " + str(normA / normB))
    print()


def main():
    print("\n1.")
    task_1(float(input("Введите a: ")), float(input("Введите b: ")))
    print("\n2.")
    task_2(float(input("Введите d: ")))
    print("\n3.")
    task_3(float(input("Введите a: ")), float(input("Введите b: ")))
    print("\n4.")
    task_4(float(input("Введите число: ")), float(input("Введите число: ")))
    print("\n5.")
    task_5(float(input("Введите число: ")), float(input("Введите число: ")))


if __name__ == '__main__':
    main()
