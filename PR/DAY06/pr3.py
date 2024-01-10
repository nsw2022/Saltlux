for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}")

lst = [1, 2, 3, 2, 1, 5, 6, 5, 5, 5, 7]
duplicatted = set()
for i in range(len(lst)):
    # i + 1 은 i 다음
    for j in range(i + 1, len(lst)):  # 현재 i 다음 모든 리스트의 요소에 접근 하겠다.
        if lst[i] == lst[j]:
            duplicatted.add(lst[i])

print(duplicatted)
