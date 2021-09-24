def getList():
    result = []
    for i in range(int(input())):
        result.append(float(input("Введите размер массива: ")))
    return result


def task_1():
    print("\n1.")
    arrA = getList()
    arrB = getList()
    for i in range(len(arrA)):
        x1 = arrA[i]
        x2 = arrB[i]
        arrA[i] = x2
        arrB[i] = x1
    print("Результат:")
    print(arrA)
    print(arrB)
    print()


def task_2():
    print("\n2.")
    arrA = getList()
    arrB = []
    summ = 0
    for i in range(len(arrA)):
        summ += arrA[i]
        arrB.append(summ / (i + 1))
    print("Результат: " + str(arrB))
    print()


def task_3():
    print("\n3.")
    arr = getList()
    lastOdd = 1
    for el in arr[::-1]:
        if el % 2 == 1:
            lastOdd = el
            break
    arr = list(map(lambda x: x if x % 2 == 0 else x * lastOdd, arr))
    print("Результат: " + str(arr))
    print()


def task_4():
    print("\n4.")
    arr = getList()
    maxN = arr[0]
    maxI = 0
    minN = arr[0]
    minI = 0
    for i in range(len(arr)):
        n = arr[i]
        if n > maxN:
            maxN = n
            maxI = i
        if n < minN:
            minN = n
            minI = i
    first = min([minI, maxI])
    last = max([minI, maxI])
    for i in range(first + 1, last):
        arr[i] = 0
    print("Результат: " + str(arr))
    print()


def task_5():
    print("\n5.")
    arr = getList()
    if len(arr) < 2:
        print("Результат: " + str(arr))
        return
    first = arr[0]
    for i in range(len(arr)):
        n = arr[i]
        if n > first:
            arr = arr[1:i] + [first] + arr[i::]
            break
    if arr[0] == first:
        arr = arr[1::]+[first]
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
