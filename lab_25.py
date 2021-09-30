def task_1():
    print("\n1.")
    f = open("text_files/lab_25_1", "r+")
    t = str(f.read())
    f.seek(0)
    f.write(t[t.index(" ") + 1::])
    f.truncate()
    print()


def task_2():
    print("\n2")
    name, n, k = input(), int(input()), int(input())
    f = open(name, "w")
    line = "*" * k
    for i in range(n):
        f.write(line + "\n")
    print()


def task_3():
    print("\n3.")
    f1 = open("text_files/lab_25_3a", "r+")
    f2 = open("text_files/lab_25_3b", "r")
    text = f2.read() + f1.read()
    f2.close()
    f1.truncate(0)
    f1.close()
    f1 = open("text_files/lab_25_3a", "w")
    f1.write(text)
    print()


def task_4():
    print("\n4.")
    f = open("text_files/lab_25_4", "r+")
    text = " ".join(f.read().split())

    f.truncate(0)
    f.close()
    f = open("text_files/lab_25_4", "w")
    f.write(text)
    print()


def task_5():
    print("\n5.")
    f = open("text_files/lab_25_5", "r")
    text = f.read()
    lines = text.split("\n")
    notEmptyLines = [line for line in lines if line.strip() != ""]
    c = 0
    for line in notEmptyLines:
        if line.startswith("     "):
            c += 1
    print("Количество абзацев: " + str(c))
    print()


def main():
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()


if __name__ == '__main__':
    main()
