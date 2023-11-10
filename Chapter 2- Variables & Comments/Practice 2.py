#Write a python program that takes courses marks as input and then calculates average of all the
#courses. After calculating the average, calculate the percentage of a student using total marks. Assume
#the total of all the courses marks is 500 or take the total marks from the user as input.
# Taking input for course marks
marks = []
for i in range(5):
    marks.append(int(input(f"Enter marks for course {i+1}: ")))

# Calculating average
average = sum(marks) / len(marks)

# Calculating percentage
total_marks = 500  # Assuming total marks as 500
percentage = (sum(marks) / total_marks) * 100

# Displaying the results
print(f"Average marks: {average}")
print(f"Percentage: {percentage}%")
