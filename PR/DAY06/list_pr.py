def find_different_values(numbers: list[int], value: int) -> list[int]:
    return [num for num in numbers if num != value]


assert find_different_values([1, 2, 3, 2, 4, 5, 2], 2) == [1, 3, 4, 5]
assert find_different_values([10, 20, 30, 40, 10, 50], 10) == [20, 30, 40, 50]
assert find_different_values([5, 6, 7, 5, 8, 9], 5) == [6, 7, 8, 9]

print(find_different_values([1, 2, 3, 2, 4, 5, 2], 2))
print(find_different_values([10, 20, 30, 40, 10, 50], 10))
print(find_different_values([5, 6, 7, 5, 8, 9], 5))
