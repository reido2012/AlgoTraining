def get_string_list():
    return list(input())

def get_alphabet_pos(char):
    return ord(char) - 97


word = get_string_list()

turns = 0
start = 0

for i in range(len(word)):
    current_char_pos = get_alphabet_pos(word[i])
    distance = abs(start - current_char_pos)

    if distance > 13:
        turns += (26 - distance)
    else:
        turns += distance

    start = current_char_pos


print(turns)
