# ANY ALL
x = [True, True, False]

if any(x):
    print('если хотя бы один Тру')
if all(x):
    print('если все Тру')
if any(x) and not all(x):
    print('хоты бы однин Тру и один Фолс')
