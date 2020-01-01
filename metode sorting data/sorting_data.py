data = [40,20,80,70,76,99,100,44,22,22]

def bubbleSort(el):
    n =len(el)

    for i in range(n):
        for j in range(0, n-i-1):
            if el[j] > el[j+1]:
                el[j], el[j+1] = el[j+1], el[j]
    
    print("Sorted array is:")
    for i in range(n):
        print("%d" %el[i])

def shellSort(el): 
  
     
    n = len(el) 
    gap = n//2
  
    
    while gap > 0: 
  
        for i in range(gap,n): 
  
             
            temp = el[i] 
  
             
            j = i 
            while  j >= gap and el[j-gap] >temp: 
                el[j] = el[j-gap] 
                j -= gap 
  
             
            el[j] = temp 
        gap //= 2

        print("Sorted array is: ")
        for i in range(n):
            print(el[i])

def qsort(arr): 
    if len(arr) <= 1:
        return arr
    else:
        return qsort([x for x in arr[1:] if x < arr[0]]) + \
               [arr[0]] + \
               qsort([x for x in arr[1:] if x >= arr[0]])

option = True
while option:
    print("""
    1.Quick Sort
    2.Shell Sort
    3.Bubble Sort
    4.exit
    """)
    option = input("pilihlah salah satu metode sorting diatas!")
    if option =="3":
        bubbleSort(data)
    elif option =="2":
        shellSort(data)
    elif option =="1":
        print("Sorted array is = ", qsort(data))
    elif option =="4":
        print("\n goodbye")
    elif option !="":
        print("\n Not Valid Choice Try again") 
        
        

    













        
  
  
 
  






