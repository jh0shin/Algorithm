def solution(cacheSize, cities):
    from collections import deque
    cache = deque()
    time = 0
    cities = list(map(lambda x: x.lower(), cities))

    if cacheSize == 0: return len(cities) * 5

    for city in cities:
        if city in cache:
            cache.remove(city)
            cache.appendleft(city)
            time += 1
        else:
            if len(cache) == cacheSize:
                cache.pop()
            cache.appendleft(city)
            time += 5
    
    return time

a = 3
b = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

if __name__=='__main__':
    print(solution(a, b))