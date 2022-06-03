def print_to_n_number(n):
    if n == 0:
        return
    print_to_n_number(n - 1)
    print(n)


print_to_n_number(996)
