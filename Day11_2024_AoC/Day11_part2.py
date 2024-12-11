# read every line from input.txt
with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

print(input)

### Solution ###

input = input[0].split()
rocks = {}
for rock in input:
    rocks[rock] = 1
for rep in range(75):
    newrocks = {}
    for rock, amount in rocks.items():
        if rock == "0":
            if "1" not in newrocks:
                newrocks["1"] = 0
            newrocks["1"] += amount
        elif len(rock) % 2 == 0:
            first_half = str(int(rock[:len(rock) // 2]))
            second_half = str(int(rock[len(rock) // 2:]))
            if first_half not in newrocks:
                newrocks[first_half] = 0
            if second_half not in newrocks:
                    newrocks[second_half] = 0
            newrocks[first_half] += amount
            newrocks[second_half] += amount
        else:
            even_rock = str(int(rock) * 2024)
            if even_rock not in newrocks:
                newrocks[even_rock] = 0
            newrocks[even_rock] += amount
    rocks = newrocks

solution = 0
for rock, amount in rocks.items():
    solution += amount
print(solution)
