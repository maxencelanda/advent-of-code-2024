data = []

with open("day2/input.txt", 'r') as file:
    for line in file:
        levels = line.split(" ")
        report = [int(level) for level in levels]
        data.append(report)


def report_is_safe(report: list, already_removed: bool) -> bool:

    new_report = report.copy()

    def check_type(a: int, b: int, type: str) -> bool:
        if type == "increasing":
            return a < b
        return a > b

    if new_report[0] < new_report[1]:
        type = "increasing"
    elif new_report[0] > new_report[1]:
        type = "decreasing"
    else:
        if already_removed:
            return False
        for i in range(len(report)):
            report_copy = new_report.copy()
            report_copy.pop(i)
            if report_is_safe(report_copy, True):
                return True
        return False
    
    for i in range(1, len(new_report)):
        if not check_type(new_report[i-1], new_report[i], type) or abs(new_report[i-1] - new_report[i]) > 3:
            if already_removed:
                return False
            for i in range(len(new_report)):
                report_copy = new_report.copy()
                report_copy.pop(i)
                if report_is_safe(report_copy, True):
                    return True
            return False

    return True


safe_reports = 0
list_safe = []

for report in data:
    if report_is_safe(report, False):
        list_safe.append(report)
        safe_reports += 1

print(safe_reports)