def even_odd(*args):
    my_list = args[:-1]
    if args[-1] == "odd":
        return [int(el) for el in my_list if el % 2 == 1]
    else:
        return [int(el) for el in my_list if el % 2 == 0]