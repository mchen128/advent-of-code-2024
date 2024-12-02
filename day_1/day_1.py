# Part 1
file = open('advent_of_code/day_1_input.txt', 'r')
lists = [[],[]]
for line in file:
    line = line.strip().split('   ')
    lists[0].append(int(line[0]))
    lists[1].append(int(line[1]))

lists[0].sort()
lists[1].sort()

sum_distance = 0
for index in range(len(lists[0])):
    distance = abs(lists[0][index] - lists[1][index])
    print()
    sum_distance = sum_distance + distance

print(sum_distance)