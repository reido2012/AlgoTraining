from itertools import permutations

def get_int():
    return int(input())

def get_int_list():
    return list(map(int, input().split()))

def get_string_list():
    return list(input())

num_teams = get_int()
all_matches = permutations(range(num_teams), 2)

# map of colors
colors = {}

for i in range(num_teams):
    colors[i] =get_int_list()

answer = 0


for home_team, away_team in list(all_matches):

    if colors[home_team][0] == colors[away_team][1]:
        answer += 1


print(answer)

