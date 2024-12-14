# read every line from input.txt

with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

print(input)
### Solution ###

width_field = 101
height_field = 103


def bfs(new_array, start, visited):
    queue = [start]
    count = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.pop(0)
        if visited[x][y]:
            continue
        visited[x][y] = True
        count += 1
        if count > 200:
            return True
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(new_array) and 0 <= ny < len(new_array[0]) and not visited[nx][ny] and new_array[nx][
                ny] == '#':
                queue.append((nx, ny))
    return False


def has_large_component(new_array):
    visited = [[False for _ in range(len(new_array[0]))] for _ in range(len(new_array))]
    for i in range(len(new_array)):
        for j in range(len(new_array[0])):
            if new_array[i][j] == '#' and not visited[i][j]:
                if bfs(new_array, (i, j), visited):
                    return True
    return False

def extract_tuples(input_string):
    parts = input_string.replace('=', ' ').replace(',', ' ').split()
    p = (int(parts[1]), int(parts[2]))
    v = (int(parts[4]), int(parts[5]))
    return p, v

def get_quadrant(x, y):
    if x <= width_field // 2 and y <= height_field // 2:
        return 0
    if x > width_field // 2 + 1 and y <= height_field // 2:
        return 1
    if x <= width_field // 2 and y > height_field // 2 + 1:
        return 2
    if x > width_field // 2 + 1 and y > height_field // 2 + 1:
        return 3

    return 4

def transform_2d_array(array):
    newarray = []
    for i in range (len(array)):
        newarray.append([])
        for j in range (len(array[0])):
            if not array[i][j]:
                newarray[i].append(".")
            else:
                newarray[i].append("#")
    return newarray


def print_christmas_tree(field):
    for row in field:
        for cell in row:
            if cell == "#":
                print('#', end='')
            else:
                print('.', end='')
        print()


field = []

for i in range (height_field):
    field.append([])
    for j in range (width_field):
        field[i].append([])

for str in input:
    p = extract_tuples(str)[0]
    v = extract_tuples(str)[1]
    field[p[1]][p[0]].append(v)

count = 1
while True:
    field2 = []
    for i in range (height_field):
        field2.append([])
        for j in range (width_field):
            field2[i].append([])
    for i in range (len(field)):
        for j in range (len(field[0])):
            for k in range (len(field[i][j]) - 1, -1, -1):
                new_x = (field[i][j][k][0] + j) % width_field
                new_y = (field[i][j][k][1] + i) % height_field
                field2[new_y][new_x].append((field[i][j][k][0], field[i][j][k][1]))
    field = []
    for i in range(height_field):
        field.append([])
        for j in range(width_field):
            field[i].append([])

    for i in range(height_field):
        for j in range(width_field):
            for k in range(len(field2[i][j]) - 1, -1, -1):
                field[i][j].append((field2[i][j][k][0], field2[i][j][k][1]))
    new_array = transform_2d_array(field)
    if has_large_component(new_array):
        print_christmas_tree(new_array)
        print(count)
    count += 1








