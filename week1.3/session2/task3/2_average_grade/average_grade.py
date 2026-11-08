# Week 1.3, Session 2: Calculate Average Grade and Write to a File

# Open 'student_data.csv' to read each student's grades
# hint: skip the header row with data[1:]
with open("student_data.csv", "r") as file:  # opens the CSV file
    data = file.readlines() 

# Read each student's grades and calculate their average grade
# hint: CSV data comes as strings, convert grade columns to int() for maths
# hint: student_data.csv has columns: ID, Name, Mathematics, Science, History
# hint: average = (maths + science + history) / 3


# Open a file called 'report.txt'
with open("report.txt", "w") as report:
    for row in data[1:]:  
        student = row.strip().split(",")

        name = student[1]  
        maths = int(student[2])  
        science = int(student[3])  
        history = int(student[4])  

        average = (maths + science + history) / 3  

        report.write(f"{name}: {average:.2f}\n")
# Write each student's name and their average grade to the report
# hint: use 'w' mode to create a fresh report each time
# hint: format averages nicely, maybe to 2 decimal places with :.2f

