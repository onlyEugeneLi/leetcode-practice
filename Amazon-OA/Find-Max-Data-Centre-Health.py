def findMaxHealthSum(health: list[int], serverType: list[int], m: int) -> int:
    hashmap = {}
    for h, t in zip(health, serverType):
        if t in hashmap:
            hashmap[t] += h
        else:
            hashmap[t] = h
    
    sum_health = list(hashmap.values())
    sum_health.sort(reverse=True) # sort() sorts the list in place

    # Find out the max health value
    max_health = 0
    # min(m, len(sum_health)): 
    # in case that allowed number of types higer than available number of types
    for i in range(min(m, len(sum_health))):
        max_health += sum_health[i]
    return max_health

health = [4, 5, 5, 6]
serverType = [1, 2, 1, 2]
m = 1
print(findMaxHealthSum(health, serverType, m))