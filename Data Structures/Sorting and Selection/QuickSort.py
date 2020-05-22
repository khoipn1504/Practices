def quickSort(inputList):
    processList = inputList.copy()      # dòng này là để thuật toán không ảnh hưởng List gốc bên ngoài
    if len(processList) < 2:
        return processList

    pivot = processList.pop()
    lowList = []
    highList = []
    for i in processList:
        if i < pivot:
            lowList.append(i)
        else:
            highList.append(i)

    return quickSort(lowList)+[pivot]+quickSort(highList)


a = [2, 5, 2, 7, 9, 0, 7, 3, 4, 67]
print(quickSort(a))
print(a)
