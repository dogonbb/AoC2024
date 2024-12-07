# read every line from input.txt
with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

print(input)

### Solution ###


def increment_ternary_string(ternary_str):
    number = int(ternary_str, 3)
    incremented_number = number + 1
    result_ternary = ""
    while incremented_number > 0:
        result_ternary = str(incremented_number % 3) + result_ternary
        incremented_number //= 3
    if len(result_ternary) < len(ternary_str):
        result_ternary = result_ternary.zfill(len(ternary_str))
    return result_ternary
solution = 0

for i in range (len(input)):
    operators = []
    number_left = input[i].split(':')[0]
    numbers_right = input[i].split(':')[1].split(" ")[1:]
    for j in range(len(numbers_right) - 1):
        operators.append("+")
    while True:

        numbers_right = input[i].split(':')[1].split(" ")[1:]

        sum_and_mult_right = 0
        sum_and_mult_right += int(numbers_right[0])

        for j in range (len(operators)):
            if operators[j] == "+":
                sum_and_mult_right += int(numbers_right[j+1])
            elif operators[j] == "*":
                sum_and_mult_right *= int(numbers_right[j + 1])
            elif operators[j] == "|":
                sum_and_mult_right = int(str(sum_and_mult_right) + numbers_right[j+1])
        if sum_and_mult_right == int(number_left):
            solution += int(sum_and_mult_right)
            break
        
        if sum_and_mult_right == int(number_left):
            solution += int(sum_and_mult_right)
            break

        if all(i == operators[0] for i in operators) and operators[0] == "|":
            break

        ter = ""
        for op in operators:
            if op == "+":
                ter += "0"
            elif op == "*":
                ter += "1"
            elif op == "|":
                ter += "2"
        number = increment_ternary_string(ter)
        for j in range (len(number)):
            if number[j] == "0":
                operators[j] = "+"
            elif number[j] == "1":
                operators[j] = "*"
            elif number[j] == "2":
                operators[j] = "|"
print(solution)