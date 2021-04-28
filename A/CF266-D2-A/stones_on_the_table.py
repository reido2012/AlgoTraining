import sys

def get_int():
    return int(input())

def get_string_list():
    return list(input())

n = get_int()
stones = get_string_list()

count = 0

for i in range(n-1):
    if stones[i] == stones[i+1]:
        count +=1

print(count)
