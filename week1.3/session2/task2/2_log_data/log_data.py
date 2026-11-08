# Week 1.3, Session 2: Log Data Filtering

# We want to find all failed login attempts based on Request and Status code 
# (i.e., POST /login with the response 401) in a log file and print these out in a
# human-readable format.
import csv

# open and read the file
try:
    with open("site.log", "r") as file:  
        reader = csv.reader(file)  
        next(reader)  


# find all failed login attempts (POST /login with the response 401)
        for row in reader: 
            date, time, ip, user_agent, request, status = row

            if request == "POST /login" and status == "401":  # checks for failed logins
                print(f"IP address {ip} failed to login at {time} on {date}") 

except FileNotFoundError:
    print("File not found")

# and print these out in a human-readable format:
# IP address 192.168.1.17 failed to login at 10:42:12 on 2024-10-20


# Hints:
# - Remember to handle file errors
# - The first row is headers - you'll need to skip it
# - Each row has: Date, Time, IP_Address, User_Agent, Request, Status_Code
# - You need to find rows where Request = "POST /login" AND Status_Code = "401"
# - You can use list comprehension or loops to filter the data