'''
Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.
'''

def lucky_sum(a,b,c):
    sum = a + b + c
    if a == 13:
        sum = sum - a - b - c
    elif b == 13:
        sum = sum - b - c
    elif c == 13:
        sum = sum - c
    return sum
    