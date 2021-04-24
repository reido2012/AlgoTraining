import sys

def get_int_list():
    return list(map(int, input().split()))

a, b, c = get_int_list()

print( "Yes" if a**2  + b **2 < c**2 else "No")
