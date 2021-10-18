def task_1():
    print("\n1.")
    char = ord(input("Введите символ С: "))
    print("Следующий символ: " + str(chr(char + 1)))
    print("Прошлый символ: " + str(chr(char - 1)))
    print()


def task_2():
    print("\n2")
    s = input("Введите строку: ")
    result = ""
    for ch in s:
        result += ch + " "
    print("Каждый символ с пробелами: " + result[0:len(result) - 1])
    print()


def task_3():
    print("\n3.")
    alphabet = "A, B, C, D, E, F, G, H, I, K, L, M, N, O, P, Q, R, S, T, V, X, Y, Z, J, U, W".split(", ")
    s = input("Введите строку: ")
    c = 0
    for ch in s:
        if ch in alphabet:
            c += 1
    print("Прописных латинских букв: " + str(c))
    print()


def task_4():
    print("\n4.")
    c = input("Введите символ С: ")
    s = input("Введите строку: ")
    result = ''
    for ch in s:
        if ch == c:
            result += c + c
            continue
        result += ch
    print("С удвоенным символом \""+c+"\": " + result)
    print()


def task_5():
    print("\n5.")
    print("Число вхождений подстроки в строку: " + str(input("Введите строку ").count(input("Введите подстроку "))))
    print()


def main():
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()


if __name__ == '__main__':
    main()
