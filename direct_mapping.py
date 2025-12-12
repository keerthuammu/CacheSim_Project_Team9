def direct_mapped_cache_sim(block_refs, cache_size):
    """
    Simulate Direct Mapping cache.

    block_refs : list of int
        sequence of memory block references
    cache_size : int
        number of lines the cache has
    """
    
    cache = [None] * cache_size

    hits = 0
    misses = 0

    print("Reference | Cache Content | Hit/Miss")
    print("------------------------------------")

    for block in block_refs:
      
        index = block % cache_size

       
        if cache[index] == block:
            hits += 1
            status = "HIT"
        else:
            misses += 1
            cache[index] = block  
            status = "MISS"

      
        print(f"{block:9} | {cache} | {status}")

    total = hits + misses
    hit_ratio = hits / total if total > 0 else 0

    print("\nTotal References:", total)
    print("Total Hits      :", hits)
    print("Total Misses    :", misses)
    print(f"Hit Ratio       : {hit_ratio:.2f}")

    return hits, misses, hit_ratio


# Example usage
if __name__ == "__main__":
    # Read user input: block references as space-separated ints
    sequence = input("Enter block references (space-separated): ")
    block_refs = list(map(int, sequence.strip().split()))

    # Ask for cache size
    cache_size = int(input("Enter number of cache lines: "))

    # Run simulation
    direct_mapped_cache_sim(block_refs, cache_size)
