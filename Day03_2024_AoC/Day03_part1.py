# read every line from input.txt
with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

print(input)

### Solution ###

solution = 0
for i in range (len(input)):
    # find last ')' in string
    dist = 0
    for k in range (len(input) -1,-1,-1):
        if input[k] != 'm':
            dist+=1

    for j in range (len(input[i]) - dist):
        if input[i][j] == 'm' and input[i][j+1] == 'u' and input[i][j+2] == 'l':
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
                else:
                    j = count
                    continue

print(solution)