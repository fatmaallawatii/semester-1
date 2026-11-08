# Week 1.3, Session 2: Validate image

# Open a pgm image
try:
    with open("../images/feep.pgm", "r") as file:  
        lines = file.readlines()  


# You could handle file errors with try/except

# Read the file content
    data = []  

    for line in lines:  
        line = line.split("#")[0].strip() 
        if line:
            data.append(line.split()) 


# Store the width, the height, and the maximum gray value

    header = [item for row in data for item in row]
    width = int(header[1]) 
    height = int(header[2])  
    max_gray = int(header[3])  

    pixels = [int(p) for p in header[4:]]  

# For each pixel, check if the pixel value is between 0 and the maximum gray value inclusive

# Check if the widths and heights are the same as specified

# 4. Print the final verdit.
#  Print `Valid image` if the widths, the heights are the same, and all pixel values between 0 and the maximum gray value inclusive
#  Print `Invalid width` if the widths are different
#  Print `Invalid height` if the heights are different
#  Print `Invalid pixel values` if any pixel values is less than 0 and greater than the maximum gray value


    # Check pixel values
    valid_pixels = all(0 <= p <= max_gray for p in pixels)  

    # Check width and height
    pixel_rows = data[3:] 
    valid_width = all(len(row) == width for row in pixel_rows)  
    valid_height = len(pixel_rows) == height  

    
    if not valid_width:
        print("Invalid width")
    elif not valid_height:
        print("Invalid height")
    elif not valid_pixels:
        print("Invalid pixel values")
    else:
        print("Valid image")

except FileNotFoundError:
    print("Image file not found") 
except (ValueError, IndexError):
    print("Invalid image data")  
