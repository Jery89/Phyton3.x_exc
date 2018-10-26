a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

size = 0

new_list = []

for x in a:
    for y in b:
        if x == y:
            new_list.append(y)

bufor = new_list[0]
index = 0

for i in range(index+1, len(new_list)):
    if i == new_list[index]:
        new_list.remove(bufor)
        bufor+1
        index+1
    else:
        bufor + 1
        index + 1
        

print('list of equal elements ')
print(new_list)
