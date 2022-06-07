def get_magic_triangle(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [[1], [1, 1]]
    else:
        ll = [[1], [1, 1]]
        i = 1
        while i <= n - 2:
            second_list = []
            second_list.append(1)
            current_list = ll[i]
            for j in range(i):
                second_list.append(current_list[j] + current_list[j + 1])
            second_list.append(1)
            ll.append(second_list)
            i += 1
    return ll
