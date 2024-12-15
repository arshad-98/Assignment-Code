def generate_series(a):
    series = []
    for i in range(1, a * 2, 2):
        series.append(i)
    return series

a = int(input("Enter a number: "))
result = generate_series(a)
print(" ".join(map(str, result)))