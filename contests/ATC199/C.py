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

flip = False

for i in range(Q):
    transformation, a, b = get_int_list()

    if transformation == 1:
        a -= 1
        b -= 1

        if flip:
            # Transform a and b to what they would be if we had swapped the
            # first N with the last N
            a = ( a + N ) % ( 2 * N )
            b = ( b + N ) % ( 2 * N )

        # Swap ath and bth charcter
        S[a], S[b] = S[b], S[a]
    else:
        # Flip between true and false
        flip = not flip

if flip:
    S[:N], S[N:] = S[N:], S[:N]

print(''.join(S))
