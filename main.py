def my_rat(a, b):
    return [a, b]


def add_rat(x, y):
    return my_rat((x[0] * y[1]) + (y[0] * x[1]), x[1] * y[1])


x = my_rat(1, 2)
y = my_rat(3, 4)
print(add_rat(x, y))



