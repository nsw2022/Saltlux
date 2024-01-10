fruits = ["사과", "바나나", "체리"]
for i, fruits in enumerate(fruits):
    print(f"index {i}: {fruits}")


fruits = ["사과", "바나나", "체리"]
for index, fruits in enumerate(fruits, 1):
    print(f"index {index}: {fruits}")
