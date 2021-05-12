def get_int_list():
    return list(map(int, input().split()))

price, r = get_int_list()

i = 1
while True:
    # r is the exact value we need or we only need 10 burle coins
    if (i * price) % 10 == r or (i * price) % 10 == 0:
        print(i)
        break

    i+=1


