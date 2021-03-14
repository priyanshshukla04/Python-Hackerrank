dict1 = {}
list1 = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    dict1[name] = score
# print(dict1)
values_dict = dict1.values()
# print(values_dict)
# print(dict1)
second_largest = sorted(list(set(values_dict)))[1]
for k,v in dict1.items():
    if (v==second_largest):
        list1.append(k)
list1.sort()
for i in range(len(list1)):
    print(list1[i])

# 4
# Sona
# -25.001
# Mona
# -25.0001
# Mini
# -25.000
# Rita
# -25.0