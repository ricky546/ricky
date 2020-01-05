data = [40, 20, 80, 70, 76, 99, 100, 44, 22, 22]


def bubbleSort(arr):
    x = arr
    n = len(x)
    sorted_data = []
    for i in range(n):
        for j in range(0, n-i-1):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]

    for i in range(n):
        sorted_data.append(x[i])
    print("Sorted array is: ", sorted_data)


def shellSort(arr):
    x = arr
    n = len(x)
    gap = n//2
    while gap > 0:
        for i in range(gap, n):
            temp = x[i]
            j = i
            while j >= gap and x[j-gap] > temp:
                x[j] = x[j-gap]
                j -= gap
            x[j] = temp
        gap //= 2
    return x


def qsort(arr):
    new_arr = arr
    if len(new_arr) <= 1:
        return new_arr
    else:
        return qsort([x for x in new_arr[1:] if x < new_arr[0]]) + \
            [new_arr[0]] + \
            qsort([x for x in new_arr[1:] if x >= new_arr[0]])


option = True
print("Data source: ", data)
while option:
    print("""
    1.Quick Sort
    2.Shell Sort
    3.Bubble Sort
    4.exit
    """)
    option = input("Pilihlah salah satu metode sorting di atas: [1/2/3/4] ")
    if option == "3":
        bubbleSort(data)
    elif option == "2":
        shellSort(data)
        sorted_data = []
        for i in range(len(data)):
            sorted_data.append(data[i])
        print("Sorted array is: ", sorted_data)
    elif option == "1":
        print("Sorted array is: ", qsort(data))
    elif option == "4":
        print("\n goodbye")
        break
    elif option != "":
        print("\n Not Valid Choice Try again")

# Question?
# Why after running shellshort, the data source changed?
