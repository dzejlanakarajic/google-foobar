def solution(l):
    result = 0

    n = len(l)

    for j in range(1, n - 1):
        a, b = 0, 0
        for i in range(j):

            if l[j] % l[i] == 0:
                a += 1

        for k in range(j + 1, n):
            if l[k] % l[j] == 0:
                b += 1
        result += a * b

    return result
