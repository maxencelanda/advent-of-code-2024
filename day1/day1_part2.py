list1 = []
list2 = []

with open("day1/input.txt", 'r') as file:
    for line in file:
        left, right = line.split("   ")
        list1.append(int(left))
        list2.append(int(right))

similarity_scores_list = []

for left_number in list1:
    similarity_score = 0
    for right_number in list2:
        if left_number == right_number:
            similarity_score += 1
    similarity_score *= left_number
    similarity_scores_list.append(similarity_score)

sum = 0

for score in similarity_scores_list:
    sum += score

print(sum)
