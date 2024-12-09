# read every line from input.txt
with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

# print(input)

### Solution ###

def remove_last_number(string):
    end_idx = len(string) - 1
    in_number = False

    for i in range(len(string) - 1, -1, -1):
        if string[i].isdigit():
            if not in_number:
                end_idx = i
                in_number = True
        elif in_number:
            return string[:i + 1] + string[end_idx + 1:]

    return string[:end_idx + 1]


original_string = input[0]
string_with_spaces = ""
for i in range (0,len(original_string), 2):
    index = int( i / 2)
    amount = original_string[i]
    for j in range (int(amount)):
        string_with_spaces += str(index)
        string_with_spaces += "_"

    if i+1 == len(original_string):
        break
    spaces = original_string[i+1]
    for j in range (int(spaces)):
        string_with_spaces += "."
        string_with_spaces += "_"

list_without_spaces_rev = string_with_spaces.replace(".","")
list_without_spaces_rev = list_without_spaces_rev.split("_")
list_without_spaces_rev.pop()
for i in range(len(list_without_spaces_rev) - 1, -1, -1):
    if list_without_spaces_rev[i] == '':
        list_without_spaces_rev.pop(i)
list_without_spaces_rev = list_without_spaces_rev[::-1]

# remove last _
string_with_spaces = string_with_spaces[:-1]
print(string_with_spaces.count("."))
for i in range (string_with_spaces.count(".")):
    string_with_spaces = string_with_spaces.replace(".", list_without_spaces_rev[i], 1)
    string_with_spaces = remove_last_number(string_with_spaces)
    if i % 1000 == 0:
        print(i)

string_with_spaces = string_with_spaces.split("_")
for i in range(len(string_with_spaces) - 1, -1, -1):
    if string_with_spaces[i] == "":
        string_with_spaces.pop(i)

solution = 0
for i in range (len(string_with_spaces)):
    solution = solution + i * int(string_with_spaces[i])

print(solution)