def BinarySearch(list, item):
    start = 0
    end = len(list)-1

    while start <= end :
        midle= start + (end-start) //2 
        compar = list[midle]
        if compar == item :
            return midle
        elif item < compar :
                end =midle -1 
        else :
            start = midle +1
    return -1
