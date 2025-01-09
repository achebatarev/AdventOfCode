from tqdm import tqdm
import sys
from collections import defaultdict, Counter

try:
    FILE = sys.argv[1]
except:
    FILE = "test.in"

# NOTE: order doesn't matter

nums = Counter(open(FILE).read().split())


for _ in tqdm(range(75)):
    new_nums = defaultdict(int) 
    for e in tqdm(nums):
        if e == "0":
            new_nums["1"] += nums[e]
        elif len(e) % 2 == 0:
            new_nums[str(int(e[:len(e)//2]))] += nums[e]
            new_nums[str(int(e[len(e)//2:]))] += nums[e]
        else:
            new_nums[(str(int(e)*2024))] += nums[e]
    nums = new_nums


print(sum(nums.values()))
