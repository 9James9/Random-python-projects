import re
phoneNumRegex = re.compile('[(\( )]?\d{3}[(\( )]?[-.,]\d{3}[-.,]\d{4}')
num = '555.222.1213, 123-456-6969'
mo = phoneNumRegex.search(f'My number is {num}')
print(mo.group())
all = phoneNumRegex.findall(num)
print(all)