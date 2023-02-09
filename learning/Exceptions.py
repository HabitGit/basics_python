import sys
#assert ('Linux' in sys.platform), "This code runs on Linux only"
#x = 10
#if x > 5:
    #raise Exception('x should not exceed 5. The value of x was: {}'.format(x))
def linux_interaction():
    assert ('Linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something')
try:
    linux_interaction()
except AssertionError as error:
    print(error)
    print('Linux function was not executed')