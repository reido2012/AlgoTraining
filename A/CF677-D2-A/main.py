import sys

def get_int_list():
    return list(map(int, input().split()))

n, h = get_int_list()
friend_heights = get_int_list()

width = n  + sum( height > h for height in friend_heights)

print(width)

