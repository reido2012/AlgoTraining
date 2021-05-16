def get_int_list():
    return list(map(int, input().split()))

def get_int():
    return int(input())

def get_string_list():
    return list(input())


seq = get_int_list()

seq.sort()

if seq[1] - seq[0] == seq[2] - seq[1]:
    print("Yes")
else:
    print("No")
