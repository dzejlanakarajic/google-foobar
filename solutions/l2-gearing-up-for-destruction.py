from fractions import Fraction


def solution(pegs):
    dist = []

    for p in range(len(pegs) - 1):
        dist += [pegs[p + 1] - pegs[p]]
    result = []
    if len(dist) % 2 == 1:
        r2 = (Fraction(dist[0], 3))
        if r2 < 0:
            return [-1,-1]
        for num in dist:
            result.append(num-r2)
        result.insert(1, r2)

    elif len(dist) % 2 == 0:
        temp = dist[:]
        while len(temp) > 2:
            temp[-1] = temp[-2] - temp[-1]
            temp.pop(-2)
        r2 = (temp[1] * 2) - temp[0]

        result = [dist[0] - r2, r2]

        while len(result) != len(dist) + 1:
            for num in range(len(dist) - 1):
                result.append(dist[num + 1] - result[num + 1])
        negatives = sum(n < 0 for n in result)
        if negatives > 0:
            return [-1, -1]
    if result[0].denominator == result[-1].denominator and result[0].numerator == result[-1].numerator * 2:
        return [result[0].numerator, result[0].denominator]

    return [-1,-1]
