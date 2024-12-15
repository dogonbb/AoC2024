# read every line from input.txt
with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

print(input)

### Solution ###
field = []
instructions = ""
for i in range (len(input)):
    if input[i] != "":
        field.append([])
        field[i] = list(input[i])
    else:
        for j in range (i + 1, len(input)):
            instructions += input[j]
        break

current_pos = [0,1]
for i in range (len(field)):
    for j in range (len(field[i])):
        if field[i][j] == "@":
            current_pos = [i,j]
            break
for i in range(len(instructions)):
    if instructions[i] == "<":
        count = 1
        while field[current_pos[0]][current_pos[1] - count] == "#" or field[current_pos[0]][current_pos[1] - count] == "O":
            if field[current_pos[0]][current_pos[1] - count] == "#":
                break
            count += 1
        if field[current_pos[0]][current_pos[1] - count] == "#":
            continue
        if field[current_pos[0]][current_pos[1] - count] == ".":
            while count != 0:
                field[current_pos[0]][current_pos[1] - count] = field[current_pos[0]][current_pos[1] - count + 1]
                count -= 1
            field[current_pos[0]][current_pos[1]] = "."
            current_pos[1] -= 1
    elif instructions[i] == ">":
        count = 1
        while field[current_pos[0]][current_pos[1] + count] == "#" or field[current_pos[0]][current_pos[1] + count] == "O":
            if field[current_pos[0]][current_pos[1] + count] == "#":
                break
            count += 1
        if field[current_pos[0]][current_pos[1] + count] == "#":
            continue
        if field[current_pos[0]][current_pos[1] + count] == ".":
            while count != 0:
                field[current_pos[0]][current_pos[1] + count] = field[current_pos[0]][current_pos[1] + count - 1]
                count -= 1
            field[current_pos[0]][current_pos[1]] = "."
            current_pos[1] += 1
    elif instructions[i] == "^":
        count = 1
        while field[current_pos[0] - count][current_pos[1]] == "#" or field[current_pos[0] - count][current_pos[1]] == "O":
            if field[current_pos[0] - count][current_pos[1]] == "#":
                break
            count += 1
        if field[current_pos[0] - count][current_pos[1]] == "#":
            continue
        if field[current_pos[0] - count][current_pos[1]] == ".":
            while count != 0:
                field[current_pos[0] - count][current_pos[1]] = field[current_pos[0] - count + 1][current_pos[1]]
                count -= 1
            field[current_pos[0]][current_pos[1]] = "."
            current_pos[0] -= 1
    elif instructions[i] == "v":
        count = 1
        while field[current_pos[0] + count][current_pos[1]] == "#" or field[current_pos[0] + count][current_pos[1]] == "O":
            if field[current_pos[0] + count][current_pos[1]] == "#":
                break
            count += 1
        if field[current_pos[0] + count][current_pos[1]] == "#":
            continue
        if field[current_pos[0] + count][current_pos[1]] == ".":
            while count != 0:
                field[current_pos[0] + count][current_pos[1]] = field[current_pos[0] + count - 1][current_pos[1]]
                count -= 1
            field[current_pos[0]][current_pos[1]] = "."
            current_pos[0] += 1
for row in field:
    print(row)
solution = 0
for i in range (len(field)):
    for j in range (len(field[0])):
        if field[i][j] == "O":
            solution += 100 * i + j
print(solution)
