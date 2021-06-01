def multi_bracket_validation(input):   
    curly_open = input.count('{')
    curly_close = input.count('}')
    round_open = input.count('(')
    round_close = input.count(')')
    sqr_open = input.count('[')
    sqr_close = input.count(']')
    open_li = [curly_open,round_open,sqr_open]
    close_li = [curly_close,round_close,sqr_close]
    tuple_res = zip(open_li,close_li)

    if (curly_open == curly_close) and (round_open == round_close) and (sqr_open == sqr_close):
        return True
    else:
        counter = 0
        for i,j in tuple_res:
            if counter == 0:
                if i < j:
                    return False
                elif j < i:
                    return False
            elif counter == 1:
                if i < j:
                    return False
                elif j < i:
                    return False
            elif counter == 2:
                if i < j:
                    return False
                elif j < i:
                    return False

            counter=counter+1