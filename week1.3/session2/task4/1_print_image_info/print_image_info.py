# Week 1.3, Session 2: Print PGM image info

# Open a pgm image file
try:
    with open("../images/feep.pgm", "r") as file:  
        lines = file.readlines() 
# You can use the relative path ../images/filename
# You could handle file errors with try/except.

# Read the file content
    data = []

    for line in lines:  
        line = line.split("#")[0].strip() 
        if line: 
            data.extend(line.split()) 

    width = int(data[1]) 
    height = int(data[2])  
    max_gray = int(data[3]) 

# print image dimension (i.e., Dimensions: width x height pixels)

# print max gray value (i.e., Max Gray Value: max_gray_value)
    print(f"Dimensions: {width} x {height} pixels")
    print(f"Max Gray Value: {max_gray}")

except FileNotFoundError:
    print("Image file not found")
