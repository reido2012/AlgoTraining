def get_int_list():
    return list(map(int, input().split()))

def get_int():
    return int(input())

def get_string_list():
    return list(input())

N = get_int()


mountain_dict = {}

for i in range(N):
    name, height = input().split(" ")
    height = int(height)
    mountain_dict[name] = height

sorted_values = sorted(mountain_dict.values())

second_highest_value = sorted_values[-2]

for name, height in mountain_dict.items():
    if height == second_highest_value:
        print(name)
        break
