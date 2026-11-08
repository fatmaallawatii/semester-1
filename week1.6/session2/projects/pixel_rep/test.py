
from image import Image

img = Image.create(3, 2, 100)

print("Original pixels:")
print(img.pixels)

img.set(0, 1, 200)

print("Modified pixels:")
print(img.pixels)

print("Pixel at (0, 1):", img.get(0, 1))

img.write_pgm("test_image.pgm")

loaded = Image.read("test_image.pgm")

print("Loaded pixels:")
print(loaded.pixels)
