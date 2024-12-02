# read every line from input.txt
with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

print(input)

### Solution ###
safe = 0

def is_list_safe(input_line, increase):
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
            return 1
    return 0

for i in range (len(input)):
    input_line = input[i].split(' ')
    increase = False
    if int(input_line[1]) < int(input_line[2]):
        increase = True
    if is_list_safe(input_line, increase) == 1:
        safe += 1
    else:
        for j in range (len(input_line)):
            input_line_copy = input_line.copy()
            input_line_copy.pop(j)
            increase = False
            if int(input_line_copy[1]) < int(input_line_copy[2]):
                increase = True
            if is_list_safe(input_line_copy, increase) == 1:
                safe += 1
                break

print(safe)