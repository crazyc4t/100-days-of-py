# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_height = 0
total_number_of_heights = 0

for height in student_heights:
    total_number_of_heights += 1
    total_height += height

average = round(total_height / total_number_of_heights)

print("The average student height is = ", average)
