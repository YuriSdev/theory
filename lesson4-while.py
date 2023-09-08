# Факториал, т.е. 5! = 1*2*3*4*5 = 120
while True:
    x = int(input('Введите значение: '))
    count = 0
    y = 1

    # не сработает, потому что х приводится к целому числу, сама идея в общем
    if x == 'exit':
        break

    while count < x:
        count += 1 # count = count + 1
        y *= count # y = y * count
    else:
        print(y)



