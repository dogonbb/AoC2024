# read every line from input.txt
with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

print(input)

### Solution ###
safe = 0
for i in range (len(input)):
    input_line = input[i].split(' ')
    increase = False
    if int(input_line[1]) < int(input_line[2]):
        increase = True
    for j in range(len(input_line) - 1):
        if abs(int(input_line[j]) - int(input_line[j + 1])) > 3:
            break
        elif increase is True:
            if int(input_line[j]) >= int(input_line[j + 1]):
                break
        elif increase is False:
            if int(input_line[j]) <= int(input_line[j + 1]):
                break
        if j == len(input_line) - 2:
            safe += 1

print(safe)