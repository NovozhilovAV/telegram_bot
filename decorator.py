# определяем функции декоратора
def check(input_func):
    def output_func(*args):
        name = args[0]
        age = args[1]    #