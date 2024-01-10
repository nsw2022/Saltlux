def flatten(data):
    output = []

    for item in data:
        if type(item) == list:
            output += flatten(item)
        else:
            output.append(item)
    return output


print(flatten([[1, 2, 3], [4, [5, 6]], 7, [8, 9]]))


for i, value in enumerate([1, 2, 3, 4, 5, 6]):
    print("{}번째 요소는 {}입니다.".format(i, value))


def call_10_times(func):
    for i in range(10):
        func()
