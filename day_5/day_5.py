import math
file = open('day_5/day_5_input.txt', 'r')

rules = []
updates = []
for line in file:
    if '|' in line:
        split_rule = line.strip().split('|')
        rules.append((split_rule[0], split_rule[1]))
    elif not line.strip():
        continue
    else:
        split_update = line.strip().split(',')
        updates.append(split_update)

# Part 1
def check_update(update, rule_list):
    for update_index in range(len(update)):
        for second_index in range(update_index + 1, len(update)):
            # print(f'({update_index},{second_index})')
            if not ((update[update_index], update[second_index]) in rule_list):
                return False
    return True

middle_sum = 0
for update in updates:
    if check_update(update, rules):
        middle_sum = middle_sum + int(update[math.floor(len(update)/2)])

print(middle_sum)

# Part 2