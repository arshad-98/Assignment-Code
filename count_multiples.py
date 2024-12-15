def count_multiples(numbers):
    counts = {i: 0 for i in range(1, 10)}
    for number in numbers:
        for i in range(1, 10):
            if number % i == 0:
                counts[i] += 1
    return counts

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
result = count_multiples(numbers)
print(result)