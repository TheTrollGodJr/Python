from PIL import Image

blackScreen = Image.open("C:/Users/thetr/Documents/Python/PictureTime/3000x5000BlackScreen.png")

img1 = Image.open("C:/Users/thetr/Documents/Python/PictureTime/img.png")
img2 = Image.open("C:/Users/thetr/Documents/Python/imgA.png")

Image.Image.paste(blackScreen, img1, (0,0))
blackScreen.save("test1.png")
Image.Image.paste(blackScreen, img2, (0,0))
blackScreen.save("test2.png")