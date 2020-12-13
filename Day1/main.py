from itertools import combinations
from math import prod

input_list = []
with open("input.txt","r") as f:
    input_list = f.readlines()
input_list = [int(line) for line in input_list]

def findProductFromSum(numbers):
    for c in combinations(input_list, numbers):
        if(sum(c) == 2020):
            return prod(c)

print(findProductFromSum(2))
print(findProductFromSum(3))