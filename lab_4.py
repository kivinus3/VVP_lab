def task_1(a, b):
    print("\n1.")
    print("Площадь: " + str(a * b))
    print("Периметр: " + str((a + b) * 2))
    print()


def task_2(d):
    print("\n2.")
    print("Длина: " + str(3.14 * d))
    print()


def task_3(a, b):
    print("\n3.")
    print("Среднее арифметическое: " + str((a + b) / 2))
    print()


def task_4(a, b):
    print("\n4.")
    sqrA = a * a
    sqrB = b * b
    print("Сумма: " + str(sqrA + sqrB))
    print("Разность: " + str(sqrA - sqrB))
    print("Произведение: " + str(sqrA * sqrB))
    print("Частное: " + str(sqrA / sqrB))
    print()


def task_5(a, b):
    print("\n5.")
    normA = abs(a)
    normB = abs(b)
    print("Сумма: " + str(normA + normB))
    print("Разность: " + str(normA - normB))
    print("Произведение: " + str(normA * normB))
    print("Частное: " + str(normA / normB))
    print()


def main():
    task_1(float(input()), float(input()))
    task_2(float(input()))
    task_3(float(input()), float(input()))
    task_4(float(input()), float(input()))
    task_5(float(input()), float(input()))


if __name__ == '__main__':
    main()
