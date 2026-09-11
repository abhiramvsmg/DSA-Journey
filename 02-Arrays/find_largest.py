def find_largest(numbers):

    if not numbers:
        return None

    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest


print(find_largest([3, 7, 2, 9, 4]))
print(find_largest([-5, -2, -10, -1]))