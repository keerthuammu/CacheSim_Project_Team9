cache_size=int(input("Enter the cache size:"))
references=list(map(int,input("Enter sequence of memory block references:").split()))
cache=[]
hit=0
miss=0
print("Ref\tCache\tStatus")
for ref in references:
    if ref in cache:
        hit+=1
        status="HIT"
    else:
        miss+=1
        status="MISS"
    if len(cache)==cache_size:
        cache.pop(0)
    cache.append(ref)
    print(ref,"\t",cache,"\t",status)
hit_ratio=hit/(hit+miss)
print("Total Hits:",hit)
print("Total Misses:",miss)
print("Hit Ratio:",round(hit_ratio,2))
