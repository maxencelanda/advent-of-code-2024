list1 = []
list2 = []

with open("day1/input.txt", 'r') as file:
    for line in file:
        left, right = line.split("   ")
        list1.append(int(left))
        list2.append(int(right))

list1.sort()
list2.sort()

sum = 0
for i in range(len(list1)):
    sum += abs(list1[i] - list2[i])

print(sum)
