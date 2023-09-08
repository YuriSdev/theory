def func1():
    for x in range(10):
        for y in range(x):
            print(y)

    # result is y = 8. because stop = 10, so it x = 9 at the end. the y = x -1