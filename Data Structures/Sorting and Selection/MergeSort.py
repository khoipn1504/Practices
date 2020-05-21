def merge(S1, S2, S):
    # merge 2 sorted lists S1 and S2 into properly list S
    i = j = 0
    while i+j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i+j] = S1[i]          # copy ith element of S1 as next item of S
            i += 1
        else:
            S[i+j] = S2[j]          # copy jth element of S1 as next item of S
            j += 1


def mergeSort(S):
    n = len(S)
    if n < 2:
        return

    # divide
    mid = n//2
    S1 = S[:mid]
    S2 = S[mid:]

    # conquer (with recursion)
    mergeSort(S1)
    mergeSort(S2)

    # merge results
    merge(S1, S2, S)


a=[2,34,43,3,345,52,6,2,34,3]
mergeSort(a)
print(a)