def xor(*variables):
    '''
    XOR definition for multiple variables
    '''
    sum_ = False
    for value in variables:
        sum_ = sum_ ^ bool(value)
    return sum_