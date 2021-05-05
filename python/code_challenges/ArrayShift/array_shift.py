import math
def adding_in_the_middile(list, value):
    new_ls= list[:math.ceil(len(list)/2)] + [value] + list[math.ceil(len(list)/2):]
    print(new_ls)
    return new_ls
