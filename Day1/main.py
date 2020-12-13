from itertools import combinations
from math import prod

input = []
with open("input.txt","r") as f:
    input = f.readlines()
input = [int(line) for line in input]

def findProductFromSum(numbers):
    for c in combinations(input, numbers):
        if(sum(c) == 2020):
            return prod(c)

print(findProductFromSum(2))
print(findProductFromSum(3))