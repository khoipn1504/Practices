def queue_time(customers, n):
    l=[0]*n
    for i in customers:
        l[l.index(min(l))]+=i
    return max(l)
    

print(queue_time([33, 1, 29, 15, 42, 23, 25, 48, 6, 10, 35, 11, 1, 39, 27], 5))