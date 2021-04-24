import sys

def get_int_list():
    return list(map(int, input().split()))

def get_int():
    return int(input())

def get_string_list():
    return list(input())

N = get_int()
S = get_string_list()
Q = get_int()

indices = list(range(1, 2*N+1))

for i in range(Q):
    transformation, a, b = get_int_list()

    if transformation == 1:
        a = a - 1 if a >=1 else a
        b = b - 1 if b >=1 else b
        indices[a], indices[b] = indices[b], indices[a]
        print(indices)
    else:
        print(indices)
        indices = list(map(lambda x: (x + N) % 2*N, indices))
        print(indices)

print(indices)
result = []
for idx in indices:
    result.append(S[idx-1])

print(''.join(result))
