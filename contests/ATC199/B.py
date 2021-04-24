import sys

def get_int_list():
    return list(map(int, input().split()))

len_sequences = get_int_list()
len_sequences = len_sequences[0]

A = get_int_list()
B = get_int_list()

if len_sequences == 1:
    print(len(range(A[0], B[0]+1)))
    sys.exit(0)

sets = [ set(range(a, b+1)) for a, b in zip(A, B)]

if  len(sets) == 2:
    set0, set1 = sets
    print(len(set0.intersection(set1)))
else:
    set0, *rest = sets
    print(len(set0.intersection(*rest)))
