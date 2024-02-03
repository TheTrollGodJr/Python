from PIL import Image
from functions import numConvert, string

def get_pixel_rgb(image_path):
    # Open the image
    img = Image.open(image_path)

    # Get the size of the image
    width, height = img.size

    # Create a list to store RGB values
    rgb_values = []

    # Iterate through each pixel
    for y in range(height):
        for x in range(width):
            # Get the RGB values of the current pixel
            rgb = img.getpixel((x, y))

            # Append the RGB values to the list
            rgb_values.append(rgb[:3])

    return rgb_values

# Example usage
image_path = "D:/Pictures/Pictures/677.png"
rgb_values = get_pixel_rgb(image_path)

# Print the RGB values of the first few pixels
#for i in range(min(5, len(rgb_values))):
#    print(f"Pixel {i + 1}: RGB = {rgb_values[i][:3]}")
#print(len(rgb_values))

with open("FileToText/output.txt", "w", encoding='utf-8') as f:
    f.write("")

count = 0
sameCount = 0
lastRGB = [0,0,0]
with open("FileToText/output.txt", "a", encoding='utf-8') as f:
    for values in rgb_values:
        if (values[0] == lastRGB[0]) and (values[1] == lastRGB[1]) and (values[2] == lastRGB[2]):
            sameCount += 1
        else:
            if sameCount > 0:
                f.write(str(sameCount))
                count += 1
                if count == 1900:
                    f.write("\n")
                    count = 0
                sameCount = 0

            lastRGB[0] = values[0]
            lastRGB[1] = values[1]
            lastRGB[2] = values[2]
            for items in values:
                #print(items)
                out = numConvert[str(items)]
                if out not in string:
                    print(f"{out} not in string")
                f.write(out)
                count += 1
                
                if count == 1900:
                    f.write("\n")
                    count = 0
    f.write("\nK")