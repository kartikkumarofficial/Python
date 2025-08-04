# You have a text file named scores.txt where each line contains a student’s full name, followed by a colon, then a comma‑separated list of their exam scores. 
# Example:
# Alice Johnson: 85, 92, 78
# Bob Smith: 90,88, 79, 95
# Charlie Lee:100, 100,100
# Write a Python script that:
# Opens and reads the file line by line.
# For each line:
# Splits off the name (everything before the :).
# Splits the scores string (everything after the :) into individual score strings.
# Converts those score strings into integers.
# Calculates:
# Total score for each student.
# Average score (rounded to 2 decimal places).
# Prints out a report like:
# Alice Johnson — Total: 255, Average: 85.00
# Bob Smith     — Total: 352, Average: 88.00
# Charlie Lee   — Total: 300, Average:100.00

# solution
file = open("scores.txt",'a+')
# created the file with content
# file.write(
#     '''Alice Johnson: 85, 92, 78
# Bob Smith: 90,88, 79, 95
# Charlie Lee:100, 100,100
# ''')


for line in file:
    name_part,score_part =  line.strip().split(":")
    scores = score_part.strip().split(",")
    scores = [int(score.strip()) for score in scores]
    total = sum(scores)
    average = total / len(scores)

print(f"{name_part.strip():<15} — Total: {total}, Average: {average:.2f}")


file.close()