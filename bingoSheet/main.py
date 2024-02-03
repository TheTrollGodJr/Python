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
        if textSize[0] > 480:
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
                textPosition = ((x - textSize[0] / 2), (y - textSize[1] / 2) + 30)
                draw.text(textPosition, text=textSplit[index], fill='black', font=font)
            else:
                textPosition = ((x - textSize[0] / 2), (y - textSize[1] / 2) - 30)
                draw.text(textPosition, text=textSplit[index], fill='black', font=font)
    elif len(textSplit) == 3:
        for index, items in enumerate(textSplit):
            textSize = textSize = draw.textsize(text=items, font=font)
            #print(index, items)
            if index == 0:
                textPosition = ((x - textSize[0] / 2), (y - textSize[1] / 2) - 60)
                draw.text(textPosition, text=textSplit[index], fill='black', font=font)
            elif index == 1:
                textPosition = ((x - textSize[0] / 2), (y - textSize[1] / 2))
                draw.text(textPosition, text=textSplit[index], fill='black', font=font)
            elif index == 2:
                textPosition = ((x - textSize[0] / 2), (y - textSize[1] / 2) + 60)
                draw.text(textPosition, text=textSplit[index], fill='black', font=font)
    else:
        for index, items in enumerate(textSplit):
            textSize = textSize = draw.textsize(text=items, font=font)
            if index == 0:
                textPosition = ((x - textSize[0] / 2), (y - textSize[1] / 2) - 90)
                draw.text(textPosition, text=textSplit[index], fill='black', font=font)
            elif index == 1:
                textPosition = ((x - textSize[0] / 2), (y - textSize[1] / 2) - 30)
                draw.text(textPosition, text=textSplit[index], fill='black', font=font)
            elif index == 2:
                textPosition = ((x - textSize[0] / 2), (y - textSize[1] / 2) + 30)
                draw.text(textPosition, text=textSplit[index], fill='black', font=font)
            elif index == 3:
                textPosition = ((x - textSize[0] / 2), (y - textSize[1] / 2) + 90)
                draw.text(textPosition, text=textSplit[index], fill='black', font=font)

def create_bingo_sheet(output_file='bingoSheet/outputs/bingo_sheet.png'):
    with open("bingoSheet/squares.txt", "r") as f:
        items = f.readlines()
    
    for i in range(len(items)):
        items[i] = items[i].replace("\n", "")

    # Shuffle the items randomly
    random.shuffle(items)

    # Create a blank image for the bingo sheet
    image_size = (2550, 3300)
    img = Image.new('RGB', image_size, color='white')
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()

    #draw table
    draw.rectangle((50,50,2500,2500), outline='black', width=8)
    draw.line((540, 50, 540, 2500), width=8, fill='black')
    draw.line((1030, 50, 1030, 2500), width=8, fill='black')
    draw.line((1520, 50, 1520, 2500), width=8, fill='black')
    draw.line((2010, 50, 2010, 2500), width=8, fill='black')
    draw.line((50, 540, 2500, 540), width=8, fill='black')
    draw.line((50, 1030, 2500, 1030), width=8, fill='black')
    draw.line((50, 1520, 2500, 1520), width=8, fill='black')
    draw.line((50, 2010, 2500, 2010), width=8, fill='black')

    y = 295
    for rows in range(5):
        x = 295
        for columns in range (5):
            try:
                if rows == 2 and columns == 2:
                    text = "free spot"
                else:
                    text = items[0]
                font = ImageFont.truetype('arial.ttf', 55)
                textSize = draw.textsize(text=text, font=font)
                
                if textSize[0] > 480:
                    writeText(text=text, draw=draw, font=font, x=x, y=y)
                else:
                    textPosition = ((x - textSize[0] / 2), (y - textSize[1] / 2))
                    draw.text(textPosition, text=text, fill='black', font=font)
                
                x += 490
                items.pop(0)
            except:
                pass
        y += 490

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
    
    pdfCanvas = canvas.Canvas(outputPath, pagesize=(2550, 3300))

    for file in itemList:
        img = Image.open(file)
        width, height = img.size
        pdfCanvas.drawInlineImage(img, 0, 0, width, height)
        pdfCanvas.showPage()
    pdfCanvas.save()



if __name__ == "__main__":
    makePDF(5)