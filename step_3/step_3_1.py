
def my_func(var1, var2):
    """ Деление двух чисел"""
    try:
        var_dell = var1 / var2

    except ZeroDivisionError:
        var_dell = "Делить на 0 нельзя"
    return var_dell


print(my_func(4, 2))
