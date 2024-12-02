# Part 1
def check_if_safe(report: list[int]):
    '''Checks report to see if it meets all "safe" requirements'''
    all_increasing = True
    all_decreasing = True
    previous_level = None
    for level in report:
        if previous_level == None:  # First element handling
            previous_level = level
            continue
        elif abs(level - previous_level) < 1 or abs(level - previous_level) > 3:  # Check difference conditions
            return False

        # Check ascending/descending conditions
        elif level > previous_level:
            all_decreasing = False
        elif level < previous_level:
            all_increasing = False
        
        if not (all_increasing or all_decreasing):
            return False
        
        previous_level = level
    return True

safe_count = 0
    
file = open('day_2/day_2_input.txt', 'r')

for line in file:
    report = line.strip().split()
    report_int : list[int] = []
    for level in report:  # convert all string to int
        report_int.append(int(level))
    
    if check_if_safe(report_int):
        safe_count = safe_count + 1

print(safe_count)
file.close()  # File needs to be closed to retry in Part 2

# Part 2

def check_problem_dampener(report: list[int]):
    '''Retries report checks with the "problem dampener", which is when a report can be safe if it meets conditions with one level removed'''
    for index in range(len(report)):
        new_report = report[:index] + report[index+1:]
        if check_if_safe(new_report):
            return True
    return False

safe_count = 0

file = open('day_2/day_2_input.txt', 'r')

for line in file:
    report = line.strip().split()
    report_int : list[int] = []
    for level in report:  # convert all string to int
        report_int.append(int(level))
    
    if check_if_safe(report_int):
        safe_count = safe_count + 1
    elif check_problem_dampener(report_int):
        safe_count = safe_count + 1

print(safe_count)
file.close()
