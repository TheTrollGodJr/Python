from PIL import Image, ImageDraw, ImageFont
import random
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

#
# USE PILLOW VERSION 9.3.0
#

def wordWrapFormat(item):
        #print(item)
        textSplit = item.split(" ")
        #print(textSplit)
        #print(textSplit[0:int(len(textSplit) / 2)])
        splitList = [" ".join(textSplit[0:int(len(textSplit) / 2)]), " ".join(textSplit[int(len(textSplit) / 2):])]
        
        return splitList

def format(item, draw, font):
    item = wordWrapFormat(item)
    finalList = []
    for i, items in enumerate(item):
        textSize = draw.textsize(text=items, font=font)
        if textSize[0] > 108:
            secondSplit = wordWrapFormat(items)
            finalList.append(secondSplit[0])
            finalList.append(secondSplit[1])
        else:
            finalList.append(items)
    #print(f"\n\n{finalList}\n\n")
    return finalList

def writeText(text, draw, font, x, y):
    textSplit = format(text, draw=draw, font=font)
    
    if len(textSplit) == 2:
        for index, items in enumerate(textSplit):
            textSize = textSize = draw.textsize(text=items, font=font)
            if index == 1:
                textPosition = ((x - textSize[0] / 2), (y - textSize[1] / 2) + 7.5)
                draw.text(textPosition, text=textSplit[index], fill='black', font=font)
            else:
                textPosition = ((x - textSize[0] / 2), (y - textSize[1] / 2) - 7.5)
                draw.text(textPosition, text=textSplit[index], fill='black', font=font)
    elif len(textSplit) == 3:
        for index, items in enumerate(textSplit):
            textSize = textSize = draw.textsize(text=items, font=font)
            #print(index, items)
            if index == 0:
                textPosition = ((x - textSize[0] / 2), (y - textSize[1] / 2) - 15)
                draw.text(textPosition, text=textSplit[index], fill='black', font=font)
            elif index == 1:
                textPosition = ((x - textSize[0] / 2), (y - textSize[1] / 2))
                draw.text(textPosition, text=textSplit[index], fill='black', font=font)
            elif index == 2:
                textPosition = ((x - textSize[0] / 2), (y - textSize[1] / 2) + 15)
                draw.text(textPosition, text=textSplit[index], fill='black', font=font)
    else:
        for index, items in enumerate(textSplit):
            textSize = textSize = draw.textsize(text=items, font=font)
            if index == 0:
                textPosition = ((x - textSize[0] / 2), (y - textSize[1] / 2) - 22.5)
                draw.text(textPosition, text=textSplit[index], fill='black', font=font)
            elif index == 1:
                textPosition = ((x - textSize[0] / 2), (y - textSize[1] / 2) - 7.5)
                draw.text(textPosition, text=textSplit[index], fill='black', font=font)
            elif index == 2:
                textPosition = ((x - textSize[0] / 2), (y - textSize[1] / 2) + 7.5)
                draw.text(textPosition, text=textSplit[index], fill='black', font=font)
            elif index == 3:
                textPosition = ((x - textSize[0] / 2), (y - textSize[1] / 2) + 22.5)
                draw.text(textPosition, text=textSplit[index], fill='black', font=font)

def create_bingo_sheet(output_file='bingoSheet/outputs/bingo_sheet.png'):
    with open("bingoSheet/squares.txt", "r") as f:
        items = f.readlines()
    
    for i in range(len(items)):
        items[i] = items[i].replace("\n", "")

    # Shuffle the items randomly
    random.shuffle(items)

    # Create a blank image for the bingo sheet
    image_size = (612, 792)
    img = Image.new('RGB', image_size, color='white')
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()

    #draw table
    draw.rectangle((10,10,602,602), outline='black', width=3)
    draw.line((128.4, 10, 128.4, 602), width=3, fill='black')
    draw.line((246.8, 10, 246.8, 602), width=3, fill='black')
    draw.line((365.2, 10, 365.2, 602), width=3, fill='black')
    draw.line((483.6, 10, 483.6, 602), width=3, fill='black')
    draw.line((10, 128.4, 602, 128.4), width=3, fill='black')
    draw.line((10, 246.8, 602, 246.8), width=3, fill='black')
    draw.line((10, 365.2, 602, 365.2), width=3, fill='black')
    draw.line((10, 483.6, 602, 483.6), width=3, fill='black')

    y = 74.2
    for rows in range(5):
        x = 74.2
        for columns in range (5):
            try:
                if rows == 2 and columns == 2:
                    text = "free spot"
                else:
                    text = items[0]
                font = ImageFont.truetype('arial.ttf', 15)
                textSize = draw.textsize(text=text, font=font)
                
                if textSize[0] > 108:
                    writeText(text=text, draw=draw, font=font, x=x, y=y)
                else:
                    textPosition = ((x - textSize[0] / 2), (y - textSize[1] / 2))
                    draw.text(textPosition, text=text, fill='black', font=font)
                
                x += 118.4
                items.pop(0)
            except:
                pass
        y += 118.4

    # Save the bingo sheet as an image
    img.save(output_file)
    print(f"\n\nBingo sheet saved as {output_file}\n\n")

def makePDF(count=int, outputPath="bingoSheet/bingoCard.pdf"):
    itemList = []
    #2550, 3300
    for i in range(count):
        create_bingo_sheet(output_file=f"bingoSheet/outputs/{i}.png")
        itemList.append(f"bingoSheet/outputs/{i}.png")
    
    print(f"\n\n{itemList}\n\n")
    
    pdfCanvas = canvas.Canvas(outputPath, pagesize=letter)

    for file in itemList:
        img = Image.open(file)
        width, height = img.size
        pdfCanvas.drawInlineImage(img, 0, 0, width, height)
        pdfCanvas.showPage()
    pdfCanvas.save()



if __name__ == "__main__":
    makePDF(6)