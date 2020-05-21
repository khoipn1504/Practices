'''
# TODO: Ví dụ 1
'''


def DNA_strand(dna):
    return dna.translate(str.maketrans("ATCG", "TAGC"))


print(DNA_strand('GCGAT'))
print(str.maketrans("ATCG", "TAGC"))


'''
# TODO: Ví dụ 2
'''
table = str.maketrans(dict.fromkeys(
    '0123456789'))  # trong str.maktrans là 1 dict chứa các cặp key cần translate to valua nào đó bằng mã ASCii
a = '1H4E835L3L5340O'.translate(table)
print(table)
