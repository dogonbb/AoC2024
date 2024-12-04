# read every line from input.txt
with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

print(input)

### Solution ###

solution = 0
for i in range (len(input)):
    for j in range (len(input[i])):
        # can i find a MAS vertically
        if i <= len(input) -3 and j <= len(input[i]) - 3:
            if (input[i][j] == "M" and input[i+1][j+1] == "A" and input[i+2][j+2] == "S") or (input[i][j] == "S" and input[i+1][j+1] == "A" and input[i+2][j+2] == "M"):
                if (input[i][j + 2] == "M" and input[i+2][j] == "S") or (input[i][j + 2] == "S" and input[i+2][j] == "M"):
                    solution += 1



print(solution)