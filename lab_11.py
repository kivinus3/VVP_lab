from math import sqrt


def task_1(a, b):
    print("\n1.")
    if a == b:
        a, b = 0, 0
    else:
        a, b = max([a, b]), max([a, b])
    print("a = " + str(a))
    print("b = " + str(b))
    print()


def task_2(a, b, c):
    print("\n2.")
    print("Сумма двух больших: " + str(a + b + c - min([a, b, c])))
    print()


def task_3(a1, a2, b1, b2, c1, c2):
    print("\n3.")
    sB = sqrt((a1 - b1) ** 2 + (a2 - b2) ** 2)
    sC = sqrt((a1 - c1) ** 2 + (a2 - c2) ** 2)
    if sC < sB:
        result = "c"
        resultS = sC
    else:
        result = "b"
        resultS = sB
    print("Ближе точка: " + result)
    print("Расстояние от ближайшей точки: " + str(resultS))
    print()


def task_4(a1, a2):
    print("\n4.")
    result = "1"
    if (a1 < 0) and (a2 > 0):
        result = "2"
    elif (a1 < 0) and (a2 < 0):
        result = "3"
    elif (a1 > 0) and (a2 < 0):
        result = "4"
    print("Координатная четверть: " + result)
    print()


def task_5(a):
    print("\n5.")
    result = ""
    if a == 0:
        print("нулевое число")
        return
    elif a > 0:
        result += "положительное "
    else:
        result += "отрицательно "
    if a % 2 == 0:
        result += "четное "
    else:
        result += "нечетное "

    print(result + "число")
    print()


def task_6(a):
    print("\n6.")
    result = ""
    if a % 2 == 0:
        result += "четное "
    else:
        result += "нечетное "
    if len(str(a)) == 2:
        result += "двузначное "
    elif len(str(a)) == 3:
        result += "трехзначное "
    else:
        result += "одинарное "
    print(result + "число")
    print()


def main():
    task_1(int(input()), int(input()))
    task_2(float(input()), float(input()), float(input()))
    task_3(float(input()), float(input()), float(input()), float(input()), float(input()), float(input()))
    task_4(float(input()), float(input()))
    task_5(int(input()))
    task_6(int(input()))


if __name__ == '__main__':
    main()
