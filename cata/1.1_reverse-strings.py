# Cata 8 lvl

# Pytonic way
def solution(string):
    string = string[::-1]
    print(string)


def solution1(string):
    for char in range(len(string) - 1, -1, -1):
        return string[char]


solution('hello')
solution('hello')
