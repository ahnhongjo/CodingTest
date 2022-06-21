import itertools

def solution(n, weak, dist):
    dist.sort(reverse=True)

    for i in range(1, len(dist) + 2):
        if i == len(dist) + 1:
            return -1
        dist_combi = list(itertools.permutations(dist, i))
        w_combi = list(itertools.combinations(weak, i))

        for dists in dist_combi:
            for ws in w_combi:
                restaurant = reset(n, weak)
                for j in range(i):
                    for k in range(dists[j] + 1):
                        restaurant[(k + ws[j]) % n] = 0
                if sum(restaurant) == 0:
                    return i
                restaurant = reset(n, weak)
                for j in range(i):
                    for k in range(dists[j] + 1):
                        restaurant[k - ws[j]] = 0
                if sum(restaurant) == 0:
                    return i


def reset(n, weak):
    restaurant = [0] * n
    for w in weak:
        restaurant[w] = 1
    return restaurant


solution(12, [1, 5, 6, 10], [1, 2, 3, 4])
