def solution(pegs):
    dist = []
    for p in range(len(pegs) - 1):
        dist += [pegs[p + 1] - pegs[p]]

    gear_radius = [dist[0] / dist[0]]

    start = 0
    while len(gear_radius) <= len(dist):
        gear_radius.append(dist[start] - gear_radius[start])
        start += 1

    while gear_radius[1] != 1:
        for num in range(len(gear_radius)):
            if num % 2 == 0:
                gear_radius[num] = gear_radius[num] + 1
            else:
                gear_radius[num] = gear_radius[num] - 1

        if any(d <= 0 for d in gear_radius):
            continue

        if gear_radius[0] == 2 * gear_radius[-1]:
            return [gear_radius[0], 1]

        elif gear_radius[0] + 1 == 2 * gear_radius[-1]:
            return [(gear_radius[0] * 3) + 1, 3]
        elif gear_radius[0] + 2 == 2 * gear_radius[-1]:
            return [(gear_radius[0] * 3) + 2, 3]

    return [-1, -1]
