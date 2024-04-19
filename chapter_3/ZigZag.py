import time, sys


indent = 0
indentIncreasing = True

try:
    while True:
        print(' ' * indent, end='')  # this line gets pushed to the right
        print('**********')
        time.sleep(.1)  # timer in between code execution
        if indentIncreasing:
            indent += 1
            if indent == 20:
                indentIncreasing = False
        else:
            indent -= 1
            if indent == 0:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
