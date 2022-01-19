def solution(cacheSize, cities):
    if cacheSize ==0:
        return 5* len(cities)

    cache = []
    answer = 0

    for i in cities:
        i.lower()
        if i in cache:
            answer +=1
            cache.remove(i)
            cache.append(i)
        else:
            if len(cache) <cacheSize:
                cache.append(i)
                answer+=5
            else:
                del cache[0]
                cache.append(i)
                answer+=5

    return answer

