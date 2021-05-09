import sys

def get_int_list():
    return list(map(int, input().split()))

def get_int():
    return int(input())

def get_string_list():
    return list(input())

N, K= get_int_list()

tmp = N

for i in range(K):
    if tmp % 200 == 0:
        tmp /= 200
    else:
        tmp = int(str(round(tmp)) + "200")

print(int(tmp))
