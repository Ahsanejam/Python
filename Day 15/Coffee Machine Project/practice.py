dict1 = {"apple": 5, "banana": 3, "orange": 2}
dict2 = {"apple": 2, "banana": 1}


# dic1_sub = [print(value) for key, value in dict1.items()]
# dic2_sub = [print(value) for key, value in dict2.items()]


# print(dict1["apple"] - dict2["apple"])

def make(m1, m2):
    for items in m2:
        m1[items] -= m2[items]
    return m1
print(make(dict1, dict2))
