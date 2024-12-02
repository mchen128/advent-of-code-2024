# Part 1
safe_count = 0

file = open('day_2/day_2_input.txt', 'r')

for line in file:
    report = line.strip().split()
    report_int : list[int] = []
    for level in report:  # convert all string to int
        report_int.append(int(level))

    safe = True
    all_increasing = True
    all_decreasing = True
    previous_level = None
    for level in report_int:
        if previous_level == None:  # First element handling
            previous_level = level
            continue
        elif abs(level - previous_level) < 1 or abs(level - previous_level) > 3:  # Check difference conditions
            safe = False
            break

        elif level > previous_level:
            all_decreasing = False
        elif level < previous_level:
            all_increasing = False
        
        if not (all_increasing or all_decreasing):
            safe = False
            break
        
        previous_level = level
    if safe:
        safe_count = safe_count + 1

print(safe_count)