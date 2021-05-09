from math import ceil

def get_int_list():
    return list(map(int, input().split()))

def get_int():
    return int(input())

t, N = get_int_list()

pos = N - 1
ans = pos + ceil((N * 100)/t)
print(ans)
