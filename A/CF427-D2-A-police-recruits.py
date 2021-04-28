
def get_int():
    return int(input())

def get_int_list():
    return list(map(int, input().split()))

n = get_int()
items = get_int_list()

police = 0
ignored = 0

for x in items:
    if x > 0:
        police += x
    else:
        # No Police and crime ocurred
        if police == 0:
            ignored += 1
        else:
            police -= 1

print(ignored)
