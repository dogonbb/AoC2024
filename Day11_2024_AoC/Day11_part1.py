# read every line from input.txt
with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

print(input)

### Solution ###

input = input[0].split()

for rep in range(25):
    for i in range(len(input) - 1, -1, -1):
        if input[i] == "0":
            input[i] = "1"
        elif len(input[i]) % 2 == 0:
            first_half = str(int(input[i][:len(input[i]) // 2]))
            second_half = str(int(input[i][len(input[i]) // 2:]))
            del input[i]
            input.append(first_half)
            input.append(second_half)
        else:
            input[i] = str(int(input[i]) * 2024)

print(len(input))