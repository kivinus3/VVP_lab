def getList():
    result = []
    for i in range(int(input())):
        result.append(int(input()))
    return result


def task_1():
    arr = getList()
    k = int(input())
    l = int(input())
    summ = 0
    for i in range(k, l + 1, 1):
        summ += arr[i]
    print("Результат: " + str((summ / (l - k + 1))))


def task_2():
    arr = getList()
    if (len(arr)) < 3:
        print("Результат: 0")
        return
    raz = (arr[0] - arr[1])
    for i in range(0, len(arr) - 2, 1):
        if not ((arr[i] - arr[i + 1]) == (arr[i + 1] - arr[i + 2])):
            print("Результат: 0")
            return
    print("Результат: " + raz)


def task_3():
    arr = getList()
    minEl = arr[0]
    for i in range(2, len(arr), 2):
        minEl = min([minEl, arr[i]])
    print("Результат: " + minEl)


def task_4():
    arr = getList()
    result = 0
    for i in range(1, len(arr) - 1, 1):
        if (arr[i] > arr[i - 1]) and (arr[i] > arr[i + 1]):
            result = i
    print(result)


def task_5():
    arr = getList()
    for i1 in range(0, len(arr) - 1, 1):
        for i2 in range(i1 + 1, len(arr)):
            if arr[i1] == arr[i2]:
                print("Результат: ", str(i1), str(i2))


def main():
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()


if __name__ == '__main__':
    main()