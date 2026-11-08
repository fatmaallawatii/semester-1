# Week 1.3, Session 2: Invert PGM image

# Open a pgm image file to read
# You can use the relative path ../images/filename
# You could handle file errors with try/except

try:
    with open("../images/feep.pgm", "r") as file:  
        lines = file.readlines() 

    
    data = [] 

    for line in lines:  
        line = line.split("#")[0].strip() 
        if line:
            data.extend(line.split()) 

    width = int(data[1]) 
    height = int(data[2]) 
    max_gray = int(data[3]) 


# Create inverted image
# the formula: invert_pixel_value = max_gray - original_pixel_value

    pixels = [int(p) for p in data[4:]]  # gets all pixel values
    inverted = [max_gray - p for p in pixels]


# write the inverted pgm image to a new file.
# Remember to include:
# - the string `P2`
# - the width and height dimensions
# - maximum gray value
# - you could convert numbers in a list to strings and join them with spaces
#   for example line = [255, 255, 0, 255, 255]
#   string_line = " ".join(str(item) for item in line)
#   # output: string_line = "255 255 0 255 255"

    with open("inverted.pgm", "w") as file:  # creates a new image file
        file.write("P2\n")  # writes the PGM format
        file.write(f"{width} {height}\n")  # writes the dimensions
        file.write(f"{max_gray}\n")  # writes the maximum gray value

        for i in range(0, len(inverted), width):  # loops through each row
            row = inverted[i:i + width]  # gets the pixels for one row
            string_line = " ".join(str(item) for item in row)  # converts pixels to a string
            file.write(string_line + "\n")  # writes the row to the file

    print("Inverted image created successfully!")

except FileNotFoundError:
    print("Image file not found")  # handles missing files
except (ValueError, IndexError):
    print("Invalid image data")  # handles invalid data


