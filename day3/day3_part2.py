import re

expression = r"mul\([0-9]{1,3},[0-9]{1,3}\)|don't\(\)|do\(\)"

def multiply(mul: str):
    nums_expression = "([0-9]{1,3})"
    x, y = re.findall(nums_expression, mul)
    return int(x) * int(y)

sum = 0
with open("day3/input.txt", 'r') as file:
    found_mul = re.findall(expression, file.read())
    print(found_mul)
    do_instruction = True
    for mul in found_mul:
        if not 'mul' in mul:
            if mul == "do()":
                do_instruction = True
            else:
                do_instruction = False
        elif do_instruction:
            sum += multiply(mul)

print(sum)
