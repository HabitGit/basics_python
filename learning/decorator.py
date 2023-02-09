def decorator(input_function):
    def output_function():
        print('*******')
        input_function()
        print('*******')
    return output_function
@decorator
def saying():
    print('Hello, my name is')
saying()