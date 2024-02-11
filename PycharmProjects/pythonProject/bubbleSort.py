
def bubbleSort(lst):
    for passnum in range(len(lst)-1,0,-1):
        for i in range(passnum):
            if lst[i]>lst[i+1]:
                temp = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = temp

lst = [10,22,56,23,79,45]
bubbleSort(lst)
print(lst)

