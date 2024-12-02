data = []

with open("day2/input.txt", 'r') as file:
    for line in file:
        levels = line.split(" ")
        report = [int(level) for level in levels]
        data.append(report)


def report_is_safe(report: list) -> bool:
    def check_type(a: int, b: int, type: str) -> bool:
        if type == "increasing":
            return a < b
        return a > b

    if report[0] < report[1]:
        type = "increasing"
    elif report[0] > report[1]:
        type = "decreasing"
    else:
        return False
    
    for i in range(1, len(report)):
        if not check_type(report[i-1], report[i], type) or abs(report[i-1] - report[i]) > 3:
            return False

    return True


safe_reports = 0

for report in data:
    if report_is_safe(report):
        safe_reports += 1

print(safe_reports)
