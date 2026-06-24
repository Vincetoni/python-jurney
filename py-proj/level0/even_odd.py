def even_or_odd(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"

for i in range(1, 11):
    print(i, even_or_odd(i))