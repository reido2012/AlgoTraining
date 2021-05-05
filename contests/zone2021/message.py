from collections import deque

T = deque('')
reverse = False

for letter in input():
    if letter == "R":
        reverse = not reverse
        continue

    if reverse:
        # If we're reversed
        if T and T[0] == letter:
            T.popleft()
        else:
            T.appendleft(letter)
    else:
        if T and T[-1] == letter:
            T.pop()
        else:
            T.append(letter)

if reverse:
    T.reverse()

print("".join(T))



