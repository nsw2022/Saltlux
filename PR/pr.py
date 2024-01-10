import random

dormitories = ["그리핀도르", "후플푸프", "레번클로", "슬리데린"]
for i in dormitories:
    selected = random.choice(dormitories)
    print(selected)
    break

for char in "abcdefghijklnmopqrstuwxyz":
    print(char, end=" ")
