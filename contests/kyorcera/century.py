import sys

def get_int_list():
    return list(map(int, input().split()))

def get_int():
    return int(input())

def get_string_list():
    return list(input())

N = get_int()

left = N
count = 0

while left > 0:
    count += 1
    left -= 100

print(count)

