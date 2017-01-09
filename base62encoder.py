''' base62 encoding in python for url shortner'''

import string
from math import floor


def toBase62(num, b = 62):
    if b <= 0 or b > 62:
        return 0
    base = string.ascii_lowercase + string.ascii_uppercase + string.digits
    r = num % b
    print('r',r)
    res = base[r];
    q = floor(num / b)
    while q:
        r = q % b
        q = floor(q / b)
        res = base[int(r)] + res
    return res

def toBase10(num, b = 62):
    base = string.ascii_lowercase + string.ascii_uppercase + string.digits
    limit = len(num)
    res = 0
    for i in range(limit):
        res = b * res + base.find(num[i])
    return res


if __name__ == '__main__':
    myencoding = toBase62(10)
    decodedvalue = toBase10(myencoding)
    print ('encoded result',myencoding)
    print ('decoded result',decodedvalue)
