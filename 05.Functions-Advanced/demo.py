# def calc_combinations(names, n, combs=[]):
#     if len(combs) == n:
#         print(", ".join(combs))
#         return
#
#     for i in range(len(names)):
#         name = names[i]
#         combs.append(name)
#         calc_combinations(names[i+1:], n, combs)
#         combs.pop()
#
#
# names = input().split(", ")
# n = int(input())
#
# calc_combinations(names, n)


# def print_comb(text, idx):
#     if idx >= len(text):
#         print("".join(text))
#         return
#     print_comb(text, idx + 1)
#     for i in range(idx + 1, len(text)):
#         text[idx], text[i] = text[i], text[idx]
#         print_comb(text, idx + 1)
#         text[idx], text[i] = text[i], text[idx]
#
#
# text = list(input())
# print_comb(text, 0)


def say_hello(times):
    if times == 0:
        return
    print(times)
    say_hello(times - 1)


say_hello(5)
