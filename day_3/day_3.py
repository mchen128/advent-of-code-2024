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

mul_regex = 'mul\(\d+,\d+\)'  # Will look for specific mul commands in the text
matches: list[str] = re.findall(mul_regex, all_text)

sum = 0
for expression in matches:
    sum = sum + evaluate_mul(expression)

print(sum)
