# read every line from input.txt
with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

print(input)

### Solution ###

solution = 0
for i in range (len(input)):
    for j in range (len(input[i])):
        if input[i][j] == 'X':
            if j >= 3: # left
                if input[i][j-3:j] == 'SAM':
                    solution += 1
                # diagoal left up
                if i >= 3:
                    if input[i-1][j-1] == 'M' and input[i-2][j-2] == 'A' and input[i-3][j-3] == 'S':
                        solution += 1
                # diagoal left down
                if i <= len(input) - 4:
                    if input[i+1][j-1] == 'M' and input[i+2][j-2] == 'A' and input[i+3][j-3] == 'S':
                        solution += 1
            if j <= len(input[i]) - 4: # right
                if input[i][j+1:j+4] == 'MAS':
                    solution += 1
                # diagoal right up
                if i >= 3:
                    if input[i-1][j+1] == 'M' and input[i-2][j+2] == 'A' and input[i-3][j+3] == 'S':
                        solution += 1
                # diagoal right down
                if i <= len(input) - 4:
                    if input[i+1][j+1] == 'M' and input[i+2][j+2] == 'A' and input[i+3][j+3] == 'S':
                        solution += 1
            if i >= 3: # above
                #print(input[i-1][j], input[i-2][j], input[i-3][j])
                if input[i-1][j] == 'M' and input[i-2][j] == 'A' and input[i-3][j] == 'S':
                    solution += 1
            if i <= len(input) - 4: # down
                #print(input[i+1][j], input[i+2][j], input[i+3][j])
                if input[i+1][j] == 'M' and input[i+2][j] == 'A' and input[i+3][j] == 'S':
                    solution += 1
print(solution)