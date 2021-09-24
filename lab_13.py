def getList():
    result = []
    for i in range(int(input("Введите размер массива: "))):
        result.append(int(input()))
    return result


def task_1():
    print("\n1.")
    price = float(input())
    for i in range(1, 11, 1):
        print("Стоимость ", str(i / 10), "кг. конфет: ", str(price * i / 10))
    print()


def task_2():
    print("\n2.")
    n = int(input())
    p = 1
    for i in range(11, n * 10 + 1, 1):
        p *= i / 10
    print("Произведение: " + str(p))
    print()


def task_3():
    print("\n3.")
    n = int(input())
    summ = 0
    for i in range(1, n + 1):
        summ += 2 * i - 1
        print("Сумма: " + str(summ))
    print()


def task_4():
    print("\n4.")
    a = float(input())
    n = int(input())
    summ = 0
    for i in range(n + 1):
        summ += a ** i
    print("Сумма степеней: " + str(summ))
    print()


def task_5():
    print("\n5.")
    a = float(input())
    n = int(input())
    rez = 0
    s = 1
    for i in range(n + 1):
        rez += (a ** i) * s
        s *= -1
    print("Значение выражения: " + str(rez))
    print()


def main():
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()


if __name__ == '__main__':
    main()
