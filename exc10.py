a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def combine(list1, list2):
    buf = [x for x in list1 for y in list2 if x == y]
    return set(buf)
print(combine(a, b))
