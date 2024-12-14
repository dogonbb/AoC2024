# read every line from input.txt
with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

print(input)

### Solution ###

width_field = 101
height_field = 103

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

quadrants = [0, 0, 0, 0, 0]
for str in input:
    p = extract_tuples(str)[0]
    v = extract_tuples(str)[1]
    new_x = (v[0] * 100 + p[0]) % width_field
    new_y = (v[1] * 100 + p[1]) % height_field
    quadrant = get_quadrant(new_x + 1, new_y + 1)
    quadrants[quadrant] += 1

print(quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])


