import random as ram
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def combine(list1, list2):
    buf = [x for x in list1 for y in list2 if x == y]
    return set(buf)
print(combine(a, b))

#test
test_tab1 = []
test_tab2 = []

for i in range(ram.randrange(1, 20)):
    test_tab1.append(ram.randrange(0, 100))

for l in range(ram.randrange(1, 20)):
    test_tab2.append(ram.randrange(0, 100))

print(combine(test_tab1, test_tab2))