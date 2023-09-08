list1 = [2, 4, 6, 8]
list2 = [-2, 4, 6, -8]

pairs = []
for x in list1:
    for y in list2:
        cur_sum = x + y
        if cur_sum == 0:
            pairs.append((x, y))


def my_func(text):
    if text == text[::-1]:
        print('y')
    else:
        print('no')

print(36/3*(8-6)/6)
