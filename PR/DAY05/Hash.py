yes_tuple_key = {(0): 1}  # 튜플 -> immutable
# no_list_key = {[0]: 1}  # 리스트 -> mutable
age_dict = {"Hoi": 9}  # 딕셔너리 객체 생성
age_dict["Kui"] = 4  # 딕셔너리에 key-value 쌍 추가
print(age_dict)
del age_dict["Hoi"]  # 특정 key 값에 해당되는 원소 제거
print(age_dict)
