def insertionSort(lst):
    for index in range(1,len(lst)):
        currentvalue = lst[index]
        position = index

        while position>0 and lst[position-1]>currentvalue:
            lst[position]=lst[position-1]
            position = position-1

        lst[position]=currentvalue

lst = [54,26,93,17,77,31,44,55,20]
insertionSort(lst)
print(lst)