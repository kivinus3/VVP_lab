def task_1(a, b):
    print("\n1.")
    print("A > 2 и B <= 3 " + str(a > 2 and b <= 3))
    print()


def task_2(a, b, c):
    print("\n2.")
    print("A < B < C " + str(a < b < c))
    print()


def task_3(a):
    print("\n3.")
    print("Является четным двузначным " + str(len(str(int(a))) == 2 and a % 2 == 0))
    print()


def task_4(a):
    print("\n4.")
    print("Цифры данного числа образуют возрастающую или убывающую последовательность"
          " " + str(int(str(a)[0]) < int(str(a)[1]) < int(str(a)[2]) or
                    int(str(a)[0]) > int(str(a)[1]) > int(str(a)[2])))
    print()


def task_5(x):
    print("\n5.")
    print("«Данное число читается одинаково слева направо и справа налево»."
          + str((str(x)[0] == str(x)[3]) and (str(x)[1] == str(x)[2])))
    print()


def task_6(a, b, c):
    print("\n6.")
    print("Треугольник со сторонами a, b, c является прямоугольным: "
          + str(((a ** 2 + b ** 2) == c ** 2) or
                ((c ** 2 + b ** 2) == a ** 2) or
                ((a ** 2 + c ** 2) == b ** 2)))
    print()


def task_7(a, b, c):
    print("\n7.")
    print("Существует треугольник со сторонами a, b, c:"
          " " + str(((a + b) < c) and ((c + b) < a) and ((a + c) < b)))
    print()


def main():
    task_1(int(input()), int(input()))
    task_2(int(input()), int(input()), int(input()))
    task_3(int(input()))
    task_4(int(input()))
    task_5(int(input()))
    task_6(int(input()), int(input()), int(input()))
    task_7(int(input()), int(input()), int(input()))


if __name__ == '__main__':
    main()
