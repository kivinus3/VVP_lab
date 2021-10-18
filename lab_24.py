def task_1():
    print("\n1.")
    text = input("Введите строку: ")
    words = text.split()
    print("Количество слов: " + str(len(words)))
    print()


def task_2():
    print("\n2")
    text = input("Введите строку: ")
    words = text.split()
    result = len(words[0])
    for word in words:
        result = min([len(word), result])
    print("Длина самого короткого слова: " + str(result))
    print()


def task_3():
    print("\n3.")
    text = input("Введите строку: ")
    words = text.split()
    for word in words:
        repeatedCh = []
        newWord = ""
        for ch in word:
            if ch in repeatedCh:
                newWord += "."
            else:
                repeatedCh.append(ch)
                newWord += ch
        text = text.replace(word, newWord, 1)
    print("После преобразования: " + str(text))
    print()
    print()


def task_4():
    print("\n4.")
    text = input("Введите строку: ")
    a = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
    c = 0
    for ch in text:
        if ch in a:
            c += 1
    print("Количество гласных букв: " + str(c))
    print()


def task_5():
    print("\n5.")
    path = input("Введите строку: ")  # "D:\\Games\\Rockstar\\gta5.exe"
    slashIndex = path[::-1].index('\\') * -1
    dotIndex = path.index('.')
    print("Файл: " + path[slashIndex:dotIndex])
    print()


def task_6():
    print("\n6.")
    path = input("Введите строку: ")  # "D:\\Games\\Rockstar\\gta5.exe"
    if path.count('\\') < 2:
        print("Последний каталог: " + str())
        return
    print("Последний каталог: " + path.split('\\')[-2])
    print()


def task_7():
    print("\n7.")
    word = input("Введите строку: ")  # "password" -> asodrwsp
    newWord = ""
    for i in range(1, len(word), 2):
        newWord += word[i]

    word = word[::-1]
    start = 0
    if len(word) % 2 == 0:
        start = 1
    for i in range(start, len(word), 2):
        newWord += word[i]
    print("Зашифрованное слово: " + newWord)
    print()


def main():
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()
    task_6()
    task_7()


if __name__ == '__main__':
    main()
