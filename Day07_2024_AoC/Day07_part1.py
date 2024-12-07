# read every line from input.txt
with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

print(input)

### Solution ###


def increment_binary_string(binary_str):
    number = int(binary_str, 2)
    incremented_number = number + 1
    result_binary = bin(incremented_number)[2:]
    if len(result_binary) < len(binary_str):
        result_binary = result_binary.zfill(len(binary_str))
    return result_binary
solution = 0

for i in range (len(input)):
    operators = []
    number_left = input[i].split(':')[0]
    numbers_right = input[i].split(':')[1].split(" ")[1:]
    for j in range(len(numbers_right) - 1):
        operators.append("+")

    while True:
        sum_and_mult_right = 0
        sum_and_mult_right += int(numbers_right[0])
        for j in range (1, len(numbers_right)):
            if operators[j - 1] == "+":
                sum_and_mult_right += int(numbers_right[j])
            elif operators[j - 1] == "*":
                sum_and_mult_right *= int(numbers_right[j])
            if int(sum_and_mult_right) > int(number_left):
                break
        if sum_and_mult_right == int(number_left):
            solution += int(sum_and_mult_right)
            break
        if all(i == operators[0] for i in operators) and operators[0] == "*":
            break
        bina = ""
        for op in operators:
            if op == "+":
                bina += "0"
            elif op == "*":
                bina += "1"
        number = increment_binary_string(bina)


        for j in range (len(number)):
            if number[j] == "0":
                operators[j] = "+"
            else:
                operators[j] = "*"
print(solution)