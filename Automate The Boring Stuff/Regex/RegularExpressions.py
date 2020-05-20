import re

#! ví dụ 1
'''
phoneNumRegex = re.compile(r'\d{10}') # tạo mẫu tìm kiếm dãy số có 10 chữ số
mess = 'This is my phone 0911272278 and 0918535222'
mo = phoneNumRegex.search(mess)
print('Phone number found: '+mo.group())

#* cách tìm tất cả và trả vè list các phần tử cần tìm
mo1=phoneNumRegex.findall(mess)
print(mo1)
'''

#! ví dụ 2
'''
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mess = 'This is my phone 091-127-2278 and 123-432-5235'
mo = phoneNumRegex.search(mess)
print('Phone number found: '+mo.group())
print(mo.group(0))
print(mo.group(1))
print(mo.group(2))
print(mo.groups())  # đưa các phần tử xác thực thành tuple
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

mo1=phoneNumRegex.findall(mess)
print(mo1)
'''

#! ví dụ 3
'''
phoneNumRegex = re.compile(r'(\(\d{3}\)) (\d{3}-\d{4})')
mess = 'This is my phone (091) 127-2278.'
mo = phoneNumRegex.search(mess)
print('Phone number found: '+mo.group())
print(mo.group(0))
print(mo.group(1))
print(mo.group(2))
'''

'''
#? Nếu có nhiều hơn 1 sđt thì sao???
#* Ở đây chỉ lấy được 1 sdt đầu tiên nó gặp
#TODO: tìm thử coi có cách nào hok
#!dùng findall() để trả về list các phần tử thỏa mãng
'''

# * Matching Multiple Groups with the Pipes "|"
#! ví dụ 4
'''
friendRegex = re.compile(r'Bob|Vinh Le')
mess = 'I saw Bob and Vinh Le go to that house.'
mo = friendRegex.search(mess)
print(mo.group())
# thay đổi thứ tự của 2 nhân vật
mess1 = 'I saw Vinh Le and Bob go to that house.'
mo1 = friendRegex.search(mess1)
print(mo1.group())
'''

#! ví dụ 5
'''
bottleRegex=re.compile(r'(polyme|copper|iron) bottle')
mess='I have a copper bottle'
mo=bottleRegex.search(mess)
print(mo.group())
'''

# * sử dụng Question mark "?"
#! ví dụ 6
'''
phoneRegex=re.compile(r'(\d{3}-)?\d{3}-\d{4}')
mo1=phoneRegex.search('My number is 415-555-4242')
print(mo1.group())
mo2=phoneRegex.search('My number is 534-4442')
print(mo2.group())
'''

#! ví dụ 7
'''
starRegex=re.compile(r'(ha)* aqualukastar') #* Dùng * khi phần tử đó có thể không có hoặc có và có thể lặp lại nhiều lần
plusRegex=re.compile(r'(ha)+ aqualukaplus') #* Dùng + khi phần tử đó lặp lại ít nhất 1 lần

mo=starRegex.search('this is aqualukastar')
print(mo.group())
mo1=starRegex.search('this is hahahaha aqualukastar')
print(mo1.group())

mo=plusRegex.search('this is ha aqualukaplus')
print(mo.group())
mo1=plusRegex.search('this is hahahaha aqualukaplus')
print(mo1.group())
'''

# * Sử dụng wildcard character "."
#! ví dụ 8
'''
atRegex=re.compile(r'.at') #* lọc ra "at" và một kí tự trước nó
mo=atRegex.findall('The cat in the hat at sat on the flat mat')
print(mo)
# ['cat', 'hat', ' at', 'sat', 'lat', 'mat']
'''

#! ví dụ 9 ( thực hành )
#  0 911-272-278
#  0 911.272.278
# +84 911 272 278
"""
phoneRegex = re.compile(r'''(
    (\d|\(\+\d{2}\)|\+\d{2})        #mã vùng
    \d{3}                         #3 số đầu
    (-|/.|\s)?                    #khoảng trắng
    \d{3}                         #3 số giữa
    (-|/.|\s)?                    #khoảng trắng
    \d{3}                         #3 số cuối
)''', re.VERBOSE)


mo=phoneRegex.findall('this is my phone number +84911272278 and (+84)911-272278')
print(mo)
"""
