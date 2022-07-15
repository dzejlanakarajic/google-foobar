def checkmod(x):
    mod = x % 4
    if mod == 0:
        return x

    elif mod == 1:
        return 1

    elif mod == 2:
        return x + 1

    elif mod == 3:
        return 0


def solution(start, length):
    result = 0

    for i in range(length):
        result ^= checkmod(start-1) ^ checkmod(start+length-i-1)
        start += length
    return result
