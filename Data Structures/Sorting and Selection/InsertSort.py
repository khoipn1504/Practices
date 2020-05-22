def insertSort(inputList):
    for i in range(1, len(inputList)):
        while i > 0 and inputList[i] < inputList[i-1]:
            inputList[i], inputList[i-1] = inputList[i-1], inputList[i]
            i -= 1
    return inputList


print(insertSort([1, 4, 2, 3, 9, 8, 7, 6, 5]))
