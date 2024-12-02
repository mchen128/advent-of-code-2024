# Part 1
file = open('day_1/day_1_input.txt', 'r')
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

#  Solution to part 1
print(f'Day 1, part 1 solution: {sum_distance}')

# Part 2
similarity_score = 0
for number in lists[0]:
    frequency = lists[1].count(number)
    similarity_score = similarity_score + number*frequency

print(f'Day 1, part 2 solution: {similarity_score}')
