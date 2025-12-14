from collections import defaultdict

def lfu_cache_simulation(references, cache_size):
    cache = []
    freq = defaultdict(int)
    hits = 0
    misses = 0

    print("\nReference\tCache Content\t\tHit/Miss\n")

    for ref in references:
        if ref in cache:
            hits += 1
            freq[ref] += 1
            status = "Hit"
        else:
            misses += 1
            if len(cache) < cache_size:
                cache.append(ref)
            else:
                # Find least frequently used item
                lfu_item = min(cache, key=lambda x: freq[x])
                cache.remove(lfu_item)
                cache.append(ref)
            freq[ref] += 1
            status = "Miss"

        print(f"{ref}\t\t{cache}\t\t{status}")

    
    print("\nTotal Hits:", hits)
    print("Total Misses:", misses)
    print("Hit Ratio:", round(hits / len(references), 2))



refs_input = input("Enter memory references (space-separated): ")
references = list(map(int, refs_input.split()))

cache_size = int(input("Enter cache size: "))

lfu_cache_simulation(references, cache_size)
