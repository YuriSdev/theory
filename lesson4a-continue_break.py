x = ''

while len(x) < 5:
    y = input('Введите символ: ')
    if y == 'a':
        print('Вы ввели "а" и это не в счет')
        continue

    if y == 'z':
        print('Вы ввели "z" значит всему конец')
        break

    x += y
else:
    print(x)

