def selectionSort(inputList):
    for i in range(0, len(inputList)-1):
        min_index = i
        for j in range(i+1, len(inputList)):
            if inputList[j] < inputList[min_index]:
                min_index = j
        if min_index != i:
            inputList[i], inputList[min_index] = inputList[min_index], inputList[i]
    return inputList

print(selectionSort([1,34,572,7,322,5,4,67,7]))
