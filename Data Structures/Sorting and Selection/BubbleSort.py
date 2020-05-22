def bubbleSort(inputList):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, len(inputList)-1):
            if inputList[i] > inputList[i+1]:
                inputList[i], inputList[i+1] = inputList[i+1], inputList[i]
                sorted = False
    return inputList

print(bubbleSort([1, 4, 2, 3, 9, 8, 7, 6, 5]))
            
