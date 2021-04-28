def get_int():
    return int(input())

def get_int_list():
    return list(map(int, input().split()))

def get_string_list():
    return list(input())

calories = get_int_list()
actions = get_string_list()

total_calories = 0

for action in actions:
    action = int(action)
    total_calories += calories[action - 1]

print(total_calories)
