import sys

# read every line from input.txt
with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

print(input)

### Solution ###

def extract_numbers(input_string):
    numbers = []
    current_number = ''

    for char in input_string:
        if char.isdigit():
            current_number += char
        elif current_number:
            numbers.append(int(current_number))
            current_number = ''

    if current_number:
        numbers.append(int(current_number))

    return numbers

def f(min, max, p, n1, n2):
    solution = 0
    solution += min*n1
    solution += max*n2
    if solution == p:
        return "equal"
    elif solution > p:
        return "high"
    elif solution < p:
        return "low"
solution_all = 0
for i in range (0, (len(input)), 4):
    solution = sys.maxsize
    A = extract_numbers(input[i])
    B = extract_numbers(input[i+1])
    P = extract_numbers(input[i+2])
    for i in range (100): #for pressing A
        for j in range (100): # for pressing B
            isXokay = f(A[0], B[0], P[0], i, j)
            isYokay = f(A[1], B[1], P[1], i, j)
            if isYokay == "equal" and isXokay == "equal":
                if solution == sys.maxsize or solution > i * 3 + j:
                    solution = i*3 + j
    if solution < sys.maxsize:
        solution_all += solution
print(solution_all)