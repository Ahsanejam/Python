student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# This is in-build function for sum of all number in lists like student_score
# total_exam_score = sum(student_scores)
# print(total_exam_score)

# sum_value = 0
# for score in student_scores:
#     sum_value += score
#
# print(sum_value)

# Find Maximum number without using in-build function
# This is in-build function for finding maximum
# print(max(student_scores))


max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)
