def luhn(temp):
    list_check = list(map(int, list(temp)))
    check_sum = 0
    for idx, value in enumerate(list_check):
        if idx % 2 == 0:
            list_check[idx] = value*2
        if list_check[idx] > 9:
            list_check[idx] -= 9
        check_sum += list_check[idx]
    return str(10 - int(str(check_sum)[-1]))


print(luhn('400000844943340'))
