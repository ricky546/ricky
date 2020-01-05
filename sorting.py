data = [40, 20, 80, 70, 76, 99, 100, 44, 22, 22]


def bubbleSort(el):
    n = len(el)
    sorted_data = []
    for i in range(n):
        for j in range(0, n-i-1):
            if el[j] > el[j+1]:
                el[j], el[j+1] = el[j+1], el[j]

    for i in range(n):
        # print("%d" % el[i])
        sorted_data.append(el[i])
    print("Sorted array is: ", sorted_data)


def shellSort(el):
    n = len(el)
    gap = n//2
    sorted_data = []

    while gap > 0:
        for i in range(gap, n):
            temp = el[i]
            j = i
            while j >= gap and el[j-gap] > temp:
                el[j] = el[j-gap]
                j -= gap
            el[j] = temp
        gap //= 2

        for i in range(n):
            sorted_data.append(el[i])
    print("Sorted array is: ", sorted_data)


def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        return qsort([x for x in arr[1:] if x < arr[0]]) + \
            [arr[0]] + \
            qsort([x for x in arr[1:] if x >= arr[0]])


option = True
while option:
    print("Data source: ", data)
    print("""
    1.Quick Sort
    2.Shell Sort
    3.Bubble Sort
    4.exit
    """)
    option = input("Pilihlah salah satu metode sorting diatas: [1/2/3/4] ")
    if option == "3":
        bubbleSort(data)
    elif option == "2":
        shellSort(data)
    elif option == "1":
        print("Sorted array is: ", qsort(data))
    elif option == "4":
        print("\n goodbye")
    elif option != "":
        print("\n Not Valid Choice Try again")
