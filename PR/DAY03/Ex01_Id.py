"""
test_t = "www.example.com"

print(test_t.strip("cmowz."))
"""

a = 3
b = 2
# a = b 다른 값이 였다가 같아짐
print(id(a), id(b))

mltiline = "산산이 부서진 이름이여\n허공 중에 헤어진 이름이여!\n불러도 주인 없는 이름이여!\n부르다가 내가 죽을 이름이여!"
print(mltiline)

season = 16
print("나는 솔로 %d기 " % season)

age = 27
print(f"제 나이는 윤석열 나이로 {age-1}살입니다.")

mbti = "INFP"
blood = "B"
introduction = "제 MBTI는 {}이고, 혈액형은 {}형입니다.".format(mbti, blood)
print(introduction)


def reverse_list(lst: list) -> list:
    print(lst.sort(reverse=True))


reverse_list([10, 20, 30, 40, 50])

tuple_A = (1, 2, 3, 4, 5)
tuple_B = ("a", "B", 10.0)
print(tuple_A.__add__(tuple_B))
