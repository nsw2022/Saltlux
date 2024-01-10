import requests

with open("C:\Saltlux\Sal_Python\PR\DAY06\example.txt", "r", encoding="utf-8") as file:
    for line in file:
        # 각 줄에 대한 처리
        print(line.strip())
