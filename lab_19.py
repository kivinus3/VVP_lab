def getList():
    result = []
    for i in range(int(input())):
        result.append(float(input()))
    return result


def task_1():
    print("\n1.")
    arr = getList()
    arrIndexesDouble = []
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            arrIndexesDouble.append(i)
    for index in arrIndexesDouble:
        arr[index] = " "
    arr = [number for number in arr if number != " "]
    print("Результат: " + str(arr))
    print()


def task_2():
    print("\n2.")
    arr = getList()
    arrSet = (set(arr))
    arrDelete = []
    for el in arrSet:
        if arr.count(el) == 2:
            arrDelete.append(el)
    arr = [number for number in arr if (number not in arrDelete)]
    print("Результат: " + str(arr))
    print()


def task_3():
    print("\n3.")
    arr = getList()
    maxI = arr.index(max(arr))
    minI = arr.index(min(arr))
    if minI < maxI:
        arr.insert(minI, 0)
        arr.insert(maxI + 2, 0)
    else:
        arr.insert(maxI, 0)
        arr.insert(minI + 2, 0)
    print("Результат: " + str(arr))
    print()


def task_4():
    print("\n4.")
    arr = getList()
    counter = 0
    for i in range(len(arr)):
        n = arr[i + counter]
        if n < 0:
            arr.insert(i + counter + 1, 0)
            counter += 1
    print("Результат: " + str(arr))
    print()


def task_5():
    print("\n5.")
    arr = getList()
    counter = 0
    for i in range(len(arr)):
        n = arr[i + counter]
        if n > 0:
            arr.insert(i + counter, 0)
            counter += 1
    print("Результат: " + str(arr))
    print()


def main():
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()


if __name__ == '__main__':
    main()
