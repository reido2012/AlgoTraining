import sys
from collections import Counter

def get_int():
    return int(input())

def get_string_list():
    return list(input())

n = get_int()
games = get_string_list()

c = Counter(games)

if c['A'] > c['D']:
    print("Anton")
    sys.exit(0)

if c['A'] == c['D']:
    print("Friendship")
    sys.exit(0)

print("Danik")
