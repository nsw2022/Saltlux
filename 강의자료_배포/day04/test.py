"""
input_str = input("단어 아무거나 입력")
charcaters = list(input_str)
print(charcaters)
print(input_str)
"""
"""
my_list = [char for char in input("단어를 입력하세요: ")]
my_list.insert(0, "".join(my_list))
print(my_list[0])
"""

"""
def sun_numbers(*args):
    return sum(args)


print(sun_numbers(1, 2, 3))
print(sun_numbers(1, 2, 3, 4, 5))
"""


import re

# 정규표현식을 컴파일하여 패턴 객체를 반환
pattern = re.compile(r"\b\w+\b")

# 정규표현식과 매치 되는 모든 문자열을 리스트로 돌려줌
finditer_result = pattern.findall("Hello world")
print("find all:", finditer_result)

# 정규표현식과 매치되는 모든 문자열을 반복 가능한 객체로 돌려줌
finditer_result = pattern.finditer("Hello world")
print("Find iter:")
for match in finditer_result:
    print(f" - {match.group}")
