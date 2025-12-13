def lru_cache_simulation(cache_size, reference_string):
    cache = []
    hits = 0
    misses = 0

    print("\nLRU Cache Simulation\n")
    print("Reference\tCache Status\t\tResult")
    print("-" * 50)

    for block in reference_string:
        if block in cache:
            hits += 1
            cache.remove(block)
            cache.append(block)
            result = "HIT"
        else:
            misses += 1
            if len(cache) >= cache_size:
                cache.pop(0)   # Remove least recently used
            cache.append(block)
            result = "MISS"

        print(f"{block}\t\t{cache}\t\t{result}")

    total = hits + misses
    hit_ratio = hits / total

    print("\nFinal Results")
    print("-" * 20)
    print("Total References :", total)
    print("Cache Hits       :", hits)
    print("Cache Misses     :", misses)
    print("Hit Ratio        :", round(hit_ratio, 2))


# Driver Code
cache_size = int(input("Enter cache size: "))
reference_string = list(map(int, input("Enter reference string: ").split()))

lru_cache_simulation(cache_size, reference_string)
