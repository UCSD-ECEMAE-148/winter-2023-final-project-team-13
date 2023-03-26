from PIL import Image

# Open the PGM file
with open('ms_map_tes.pgm', 'rb') as f:
    # Convert this into a JPG file
    img = Image.open(f)
    img.load()

# Save the image as a JPEG
img.save('ms_MAP.jpg')
