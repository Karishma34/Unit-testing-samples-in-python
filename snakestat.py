#Test-set 1 - Mean
def mean(values):
    total = 0
    
    if len(values)==0:
        return total
    else:

        for i in range(len(values)):
            total += values[i]
        return total / len(values)


def sdev(values):
    if(len(values)==0):
        return 0
    variance = sum([((x - mean(values)) ** 2)for x in values]) / len(values)
    standard_deviation = variance ** 0.5
    return standard_deviation

#Test-set 2 - Greatest Common Divisor
def findGCD(val1, val2):
    if(val1<0 or val2<0):
        val1 = abs(val1)
        val2 = abs(val2)
    if (val1 == 0):
        return val2
    if (val2 == 0):
        return val1
    if (val1 == val2):
        return val1
    if (val1 > val2):
        return findGCD(val1-val2, val2)
    return findGCD(val1, val2-val1)

#Test-set 3 - Median
    
def median(val):
    val.sort()
    pos = 0
    if (len(val)%2 == 1):
        pos_odd = (pos + (len(val) + 1) / 2) - 1
        pos_odd = int(pos_odd)
        return val[pos_odd]
    elif (len(val) == 0):
        return 0 
    if(len(val)%2 == 0):
        pos_int_1_even = pos + len(val)/2 - 1
        pos_int_1_even = int(pos_int_1_even)
        pos_int_2_even = pos + len(val)/2
        pos_int_2_even = int(pos_int_2_even)
        even_val = (val[pos_int_1_even] + val[pos_int_2_even]) / 2
        return even_val 

    

