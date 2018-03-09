#!/usr/bin/python3
'''99 bottles of beer song lyrics printing program'''
lyrics = ''
for num in reversed(range(1, 100)):
    if num == 1:
        lyrics += ("{0} bottle of beer on the wall, {0} bottle of beer.\n"
                   "Take one down and pass it around, no more bottles of beer "
                   "on the wall.".format(num))
        break
    lyrics += ("{0} bottles of beer on the wall, {0} bottles of beer.\n"
               "Take one down and pass it around, {1} bottles of beer"
               " on the wall.\n\n".format(num, num - 1))
if __name__ == '__main__':
    print(lyrics)
