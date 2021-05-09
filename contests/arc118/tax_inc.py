from math import floor

def get_int_list():
    return list(map(int, input().split()))

def get_int():
    return int(input())

t, N = get_int_list()

ans_num = 0
ans = None
prev_tax_price = None
price = 1

while True:
    if ans_num == N:
        print(ans)
        break

    curr_tax_price = floor(((100 + t)/100)*price)

    if prev_tax_price and curr_tax_price - prev_tax_price > 1:
        ans_num +=1
        # Not sure about below
        ans = curr_tax_price - 1

    prev_tax_price = curr_tax_price
    price += 1
