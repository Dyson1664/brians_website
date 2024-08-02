import textwrap

def wrap(string, max_width):
    a = textwrap.wrap(string, max_width)

    return a

for i in wrap('ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4):
    print(''.join(i))