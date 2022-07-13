def solution(xs):
    if len(xs) == 0:
        return str(0)
    if len(xs) == 1:
        return str(xs[0])

    max_product = 1

    positive = [x for x in xs if x > 0]
    negative = [x for x in xs if x < 0]

    if len(positive) == 0 and len(negative) == 1:
        max_product = 0

    negative_sorted = sorted(negative)
    if len(negative_sorted) % 2 == 1:
        negative_sorted = negative_sorted[:-1]

    negative_product = []

    while len(negative_sorted) >= 2:
        negative_product += [negative_sorted[0] * negative_sorted[1]]
        negative_sorted = negative_sorted[2:]

    positive += negative_product
    positive_sorted = sorted(positive, reverse=True)

    if len(positive_sorted) >= len(xs):
        positive_sorted = positive_sorted[:-1]
        for i in positive_sorted:
            max_product *= i
    else:
        for i in positive_sorted:
            max_product *= i

    return str(max_product)
