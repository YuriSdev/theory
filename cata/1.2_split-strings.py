# Cata 6 lvl

# Complete the solution so that it splits the string into pairs of two characters.
# If the string contains an odd number of characters then it should replace
# the missing second character of the final pair with an underscore ('_').
#
# Examples:
#
# * 'abc' =>  ['ab', 'c_']
# * 'abcdef' => ['ab', 'cd', 'ef']


def solution(s):
    s = s.replace(" ", "")
    if len(s) % 2 == 0:
        print('is odd')
    elif len(s) % 2 != 0:
        s = s + '_'
        print(s, ' is not odd')
    else:
        print('something')

    print(s)


solution('ff gg ddd')

some = 2
if some == 1:
    print('some')
else:  print('ss')