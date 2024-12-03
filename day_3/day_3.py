import re
import pprint

# Part 1
def evaluate_mul(expression: str):
    [multiplicand, multiplier] = expression.strip('mul(').strip(')').split(',')
    [multiplicand, multiplier] = [int(multiplicand), int(multiplier)]
    return multiplicand*multiplier

all_text = ''
file = open('day_3/day_3_input.txt', 'r')

for line in file:
    all_text = all_text + line

file.close()  

MUL_REGEX = 'mul\(\d+,\d+\)'  # Will look for specific mul commands in the text
matches: list[str] = re.findall(MUL_REGEX, all_text)

sum = 0
for expression in matches:
    sum = sum + evaluate_mul(expression)

print(f'Day 3, Part 1: {sum}')


# Part 2
split_text_by_do = all_text.split('do()')

sum = 0
for list_item in split_text_by_do:
    if "don't()" in list_item:
        split_item = list_item.split("don't()")
        item_matches = re.findall(MUL_REGEX, split_item[0])
        
    else:
        item_matches = re.findall(MUL_REGEX, list_item)
    for expression in item_matches:
        sum = sum + evaluate_mul(expression)
print(f'Day 3, Part 2: {sum}')