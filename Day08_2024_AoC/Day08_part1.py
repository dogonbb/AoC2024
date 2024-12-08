# read every line from input.txt
with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

print(input)

### Solution ###
map_for_antinodes = [['.' for _ in range(len(input[0]))] for _ in range(len(input))]
locations = {}
for i in range (len(input)):
    for j in range (len(input[i])):
        if input[i][j] != '.':
            if input[i][j] in locations:
                locations[input[i][j]].append((j, i)) # x, y
            else:
                locations[input[i][j]] = []
                locations[input[i][j]].append((j, i)) # x, y




for key, value in locations.items():
    for i in range (len(value)):
        for j in range (i + 1, len(value)):
            diff_x = abs(value[i][0] - value[j][0])
            diff_y = abs(value[i][1] - value[j][1])
            if value[i][0] > value[j][0]:
                # up right
                new_x = value[i][0] + diff_x
                new_y = value[i][1] - diff_y
                if new_x >= 0 and new_x < len(map_for_antinodes[0]) and new_y >= 0 and new_y < len(map_for_antinodes):
                    map_for_antinodes[new_y][new_x] = "#"
                # down left
                new_x = value[j][0] - diff_x
                new_y = value[j][1] + diff_y
                if new_x >= 0 and new_x < len(map_for_antinodes[0]) and new_y >= 0 and new_y < len(map_for_antinodes):
                    map_for_antinodes[new_y][new_x] = "#"
            if value[j][0] > value[i][0]:
                # down right
                new_x = value[j][0] + diff_x
                new_y = value[j][1] + diff_y
                if new_x >= 0 and new_x < len(map_for_antinodes[0]) and new_y >= 0 and new_y < len(map_for_antinodes):
                    map_for_antinodes[new_y][new_x] = "#"
                # up left
                new_x = value[i][0] - diff_x
                new_y = value[i][1] - diff_y
                if new_x >= 0 and new_x < len(map_for_antinodes[0]) and new_y >= 0 and new_y < len(map_for_antinodes):
                    map_for_antinodes[new_y][new_x] = "#"
            if value[j][0] == value[i][0]:
                new_x = value[j][0]
                # up
                new_y = value[i][1] - diff_y
                if new_x >= 0 and new_x < len(map_for_antinodes[0]) and new_y >= 0 and new_y < len(map_for_antinodes):
                    map_for_antinodes[new_y][new_x] = "#"
                # down
                new_y = value[j][1] + diff_y
                if new_x >= 0 and new_x < len(map_for_antinodes[0]) and new_y >= 0 and new_y < len(map_for_antinodes):
                    map_for_antinodes[new_y][new_x] = "#"
solution = 0


for row in map_for_antinodes:
    for field in row:
        if field == "#":
            solution += 1
print(solution)