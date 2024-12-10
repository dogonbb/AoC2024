# read every line from input.txt
with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

print(input)

### Solution ###

def rec(input, pos, visited_nines):
    value = input[pos[0]][pos[1]]
    solution = 0
    if value == "9" and pos not in visited_nines:
        visited_nines.append([pos[0],pos[1]])
        return 1

    if pos[0] > 0 and int(input[pos[0] - 1][pos[1]]) - 1 == int(value):
        solution += rec(input, [pos[0] - 1, pos[1]], visited_nines)
    if pos[0] < len(input) - 1 and int(input[pos[0] + 1][pos[1]]) - 1 == int(value):
        solution += rec(input, [pos[0] + 1, pos[1]], visited_nines)
    if pos[1] > 0 and int(input[pos[0]][pos[1] - 1]) - 1 == int(value):
        solution += rec(input, [pos[0], pos[1] - 1], visited_nines)
    if pos[1] < len(input[0]) - 1 and int(input[pos[0]][pos[1] + 1]) - 1 == int(value):
        solution += rec(input, [pos[0], pos[1] + 1], visited_nines)
    return solution


solution = 0
for i in range (len(input)):
    for j in range (len(input[0])):
        if input[i][j] == "0":
            solution += rec(input, [i,j], [])

print(solution)