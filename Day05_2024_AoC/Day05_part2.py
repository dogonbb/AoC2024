import math

# read every line from input.txt
with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

print(input)

### Solution ###


def bring_in_right_order(number, rule_order):
    for j in range (len(number) - 1):
        number_one = number[j]
        number_two = number[j+1]
        for rule in rule_order:
            rule_number = rule.split('|')
            if rule_number[0] == number_one and rule_number[1] == number_two:
                break
            elif rule_number[0] == number_two and rule_number[1] == number_one:
                temp = number[j]
                number[j] = number[j+1]
                number[j+1] = temp
                return bring_in_right_order(number, rule_order)
    return number

rule_order = []
sites = []
index = 0
while input[index] != '':
    rule_order.append(input[index])
    index+=1

for j in range (index + 1, (len(input))):
    sites.append(input[j])

solution = 0

for i in range (len(sites)):
    number = sites[i].split(',')
    isRight = True
    for j in range (len(number) - 1):
        number_one = number[j]
        number_two = number[j+1]
        for rule in rule_order:
            rule_number = rule.split('|')
            if rule_number[0] == number_one and rule_number[1] == number_two:
                break
            elif rule_number[0] == number_two and rule_number[1] == number_one:
                isRight = False

                break
        if isRight is False:
            number = bring_in_right_order(number, rule_order)
            solution += int(number[math.floor(len(number) / 2)])
            # order in right order
            break


print(solution)