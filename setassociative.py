import math
import random
from collections import deque 

class SetAssociativeCache:

    def __init__(self, num_sets, associativity, replacement_policy):

        self.NUM_SETS = num_sets
        self.ASSOCIATIVITY = associativity
        self.POLICY = replacement_policy.upper()
        
        self.cache = [[] for _ in range(num_sets)]
        
        if self.POLICY == 'FIFO':
            self.fifo_queues = [deque() for _ in range(num_sets)]

        self.hits = 0
        self.misses = 0

        print(f"--- Cache Initialized ---")
        print(f"Config: {self.ASSOCIATIVITY}-way, {self.NUM_SETS} sets, Policy: {self.POLICY}")

    def _get_block_number_and_tag(self, block_reference):

        block_number = block_reference
        

        tag = block_number // self.NUM_SETS
        
        return block_number, tag

    def access_block(self, block_reference):

        block_number, tag = self._get_block_number_and_tag(block_reference)
        

        set_index = block_number % self.NUM_SETS
        current_set = self.cache[set_index]
        
        print(f"\nAccessing Block: {block_number} (Set: {set_index}, Tag: {tag})", end=" | ")
        

        for i, (stored_block_number, stored_tag) in enumerate(current_set):
            if stored_block_number == block_number:

                self.hits += 1
                print("Result: HIT")
                

                if self.POLICY == 'LRU':

                    hit_block = current_set.pop(i)
                    current_set.insert(0, hit_block)
                
                return "HIT"


        self.misses += 1
        print("Result: MISS", end=" | ")
        

        new_block = (block_number, tag)
        

        if len(current_set) < self.ASSOCIATIVITY:
            current_set.insert(0, new_block)
            if self.POLICY == 'FIFO':
                self.fifo_queues[set_index].append(block_number)
            print(f"Loaded Tag: {tag} (Free Space)")
        

        else:
            evicted_block_number = None
            
            if self.POLICY == 'LRU':

                evicted_block = current_set.pop()
                evicted_block_number = evicted_block[0]
            
            elif self.POLICY == 'FIFO':

                evicted_block_number = self.fifo_queues[set_index].popleft()
                

                for i, (b_num, b_tag) in enumerate(current_set):
                    if b_num == evicted_block_number:
                        current_set.pop(i)
                        break

                self.fifo_queues[set_index].append(block_number) 
                
            elif self.POLICY == 'RANDOM':

                victim_index = random.randrange(self.ASSOCIATIVITY)
                evicted_block = current_set.pop(victim_index)
                evicted_block_number = evicted_block[0]
            
            print(f"Evicted Block: {evicted_block_number} ({self.POLICY}) -> Loaded Tag: {tag}")
            current_set.insert(0, new_block) 

        return "MISS"


    def print_cache_state(self):
        print("\n=== CURRENT CACHE STATE ===")
        for i, set_data in enumerate(self.cache):

            blocks_info = [f"B:{bn}, T:{bt}" for bn, bt in set_data]
            print(f"Set {i}: [MRU/Newest] {blocks_info} [LRU/Oldest]")
        print("===========================")


    def display_stats(self):
        total_accesses = self.hits + self.misses
        hit_ratio = self.hits / total_accesses if total_accesses > 0 else 0
        
        print("\n--- Final Statistics (Step 11) ---")
        print(f"Total Hits: {self.hits}")
        print(f"Total Misses: {self.misses}")
        print(f"Total Accesses: {total_accesses}")

        print(f"Hit Ratio: {hit_ratio:.4f}")

C_WAY = 2
NUM_SETS = 4
POLICY = 'LRU'

cache = SetAssociativeCache(
    num_sets=NUM_SETS, 
    associativity=C_WAY, 
    replacement_policy=POLICY
)

block_references = [1, 5, 1, 9, 5, 13] 

print("\n--- Starting Trace Execution (Step 8) ---")

for block in block_references:
    cache.access_block(block)


cache.print_cache_state()


cache.display_stats()

