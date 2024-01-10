for i in range(2, 10, 3):
    for j in range(1, 10):
        for k in range(3):
            num = i + k
            if num < 10:
                print(num, "X", j, "=", num * j, end="\t")
        print()
    print()
