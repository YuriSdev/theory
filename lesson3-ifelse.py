x = 1

if x == 0:  # if not (..true) = false
    print('x is zero')
    x = 1
# кохоз из гайда
# elif type(x) == type(5) or type(x) == type(5.0):
elif isinstance(x, (int, float)):  # или проверка на один тип isistance(x, int)
    print('x is int or float')
else:
    print('x is another datatype')



