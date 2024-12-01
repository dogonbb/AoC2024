# read every line from input.txt
with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

print(input)

### Solution ###

for i in range (len(input)):
    input[i] = input[i].split('   ')


input1 = []
input2 = []
for i in range (len(input)):
    input1.append(input[i][0])
    input2.append(input[i][1])

input1 = sorted(input1)
input2 = sorted(input2)

solution = []
for i in range (len(input1)):
    solution.append(abs(int(input1[i]) - int(input2[i])))

solution_part_1 = 0

for i in range (len(solution)):
    solution_part_1 += solution[i]

print(solution_part_1)