
# numpy and array. 

# [10, 23, 45, 70, 11]
# return the target index if present. 
my_list = [10, 23, 45, 70, 11]
target = 70

def linear_search(my_list, target):
    size = len(my_list)
    for index in range(0, size):
        if (target == my_list[index]):
            return index
    return -1

result = linear_search(my_list, target)


