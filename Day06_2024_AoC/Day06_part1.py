# read every line from input.txt
with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

print(input)

### Solution ###

def print_grid(input, guard_pos_and_dir):
    for i in range(len(input)):
        string = ""
        for j in range(len(input[i])):
            if j == guard_pos_and_dir[0] and i == guard_pos_and_dir[1]:
                string += guard_pos_and_dir[2]
            else:
                string += input[i][j]
        print(string ,"")
    print("\n")


def make_one_move(guard_pos_and_dir, input):
    solution = 0

    while True:
        if(input[guard_pos_and_dir[1]][guard_pos_and_dir[0]] != '#' and input[guard_pos_and_dir[1]][guard_pos_and_dir[0]] != 'X'):
            input[guard_pos_and_dir[1]] = input[guard_pos_and_dir[1]][:guard_pos_and_dir[0]] + 'X' + input[guard_pos_and_dir[1]][guard_pos_and_dir[0] + 1:]
            solution += 1
        if guard_pos_and_dir[2] == 'u':
            if guard_pos_and_dir[1] > 0 and input[guard_pos_and_dir[1] - 1][guard_pos_and_dir[0]] != '#':
                guard_pos_and_dir[1] = guard_pos_and_dir[1] - 1
            elif guard_pos_and_dir[1] == 0:
                break
            elif input[guard_pos_and_dir[1] - 1][guard_pos_and_dir[0]] == '#':
                guard_pos_and_dir[2] = 'r'
        elif guard_pos_and_dir[2] == "r":
            if guard_pos_and_dir[0] < len(input[0]) - 1 and input[guard_pos_and_dir[1]][guard_pos_and_dir[0] + 1]  != '#':
                guard_pos_and_dir[0] = guard_pos_and_dir[0] + 1
            elif guard_pos_and_dir[0] == len(input[0]) - 1:
                break
            elif input[guard_pos_and_dir[1]][guard_pos_and_dir[0] + 1] == '#':
                guard_pos_and_dir[2] = 'd'
        elif guard_pos_and_dir[2] == "d":
            if guard_pos_and_dir[1] < len(input) - 1 and input[guard_pos_and_dir[1] + 1][guard_pos_and_dir[0]]  != '#':
                guard_pos_and_dir[1] = guard_pos_and_dir[1] + 1
            elif guard_pos_and_dir[1] == len(input) - 1:
                break
            elif input[guard_pos_and_dir[1] + 1][guard_pos_and_dir[0]] == '#':
                guard_pos_and_dir[2] = 'l'
        elif guard_pos_and_dir[2] =="l":
            if guard_pos_and_dir[0] > 0 and input[guard_pos_and_dir[1]][guard_pos_and_dir[0] - 1]  != '#':
                guard_pos_and_dir[0] = guard_pos_and_dir[0] - 1
            elif guard_pos_and_dir[0] == 0:
                break
            elif input[guard_pos_and_dir[1]][guard_pos_and_dir[0] - 1]  == '#':
                guard_pos_and_dir[2] = 'u'
    return solution
guard_pos_and_dir = [] # [x,y,dir] dir = u,r,d,l
for i in range (len(input)):
    for j in range (len(input[i])):
        if input[i][j] != '#' and input[i][j] != '.':
            guard_pos_and_dir.append(j)
            guard_pos_and_dir.append(i)
            guard_pos_and_dir.append("u")
solution = make_one_move(guard_pos_and_dir, input)
print(solution )