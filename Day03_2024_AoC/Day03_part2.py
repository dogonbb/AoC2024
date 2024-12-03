# read every line from input.txt
with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

print(input)

### Solution ###

do = True
solution = 0
for i in range (len(input)):
    dist = 0
    for k in range (len(input) -1,-1,-1):
        if input[k] != 'm':
            dist+=1
    for j in range (len(input[i]) - dist):
        if input[i][j] == 'm' and input[i][j+1] == 'u' and input[i][j+2] == 'l' and do is True:
            if input[i][j+3] == '(':
                first_number = ""
                count = j + 4
                while input[i][count].isdigit():
                    first_number+=input[i][count]
                    count+=1
                if first_number == "":
                    j = count
                    continue
                if int(first_number) > 999:
                    j = count
                    continue
                if input[i][count] == ',':
                    count += 1
                else:
                    j = count
                    continue
                second_number = ""
                while input[i][count].isdigit():
                    second_number += input[i][count]
                    count+=1
                if second_number == "":
                    j = count
                    continue
                if int(second_number) > 999:
                    j = count
                    continue
                if input[i][count] == ')':
                    solution += int(first_number)*int(second_number)
                    j = count
                    continue
                else:
                    j = count
                    continue
        if input[i][j] == 'd' and input[i][j+1] == 'o' and input[i][j+2] == 'n' and input[i][j + 3] == '\'' and input[i][j+4] == 't' and input[i][j+5] == '(' and input[i][j+6] == ')':
            do = False
        elif input[i][j] == 'd' and input[i][j+1] == 'o' and input[i][j+2] == '(' and input[i][j+3] == ')':
            do = True

print(solution)