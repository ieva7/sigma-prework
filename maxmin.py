list1 = [2, 4, 1, 0, 2, -1]
list2 = [20, 50, 12, 6, 14, 8]
list3 = [100, -100]

def find_min_max (list0):
    minimum = list0[0]
    maximum = list0[1]
    
    for number in list0:
        if number > maximum:
            maximum = number
        if number < minimum:
            minimum = number

    return [minimum, maximum]

print(find_min_max(list1))
print(find_min_max(list2))
print(find_min_max(list3))