def sort(lis):
    for i in range(len(lis)):
        print(i)
        j = i - 1
        temp = lis[i]

        while j >= 0 and temp < lis[j]:
            lis[j + 1] = lis[j]
            j -= 1
        lis[j + 1] = temp
    return lis
sort([5,6,1,3])