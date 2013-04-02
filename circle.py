from PIL import Image, ImageDraw

img = Image.new('RGBA', (100, 100), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)
draw.ellipse((0, 0, 100, 100), fill="blue") #draws a circle

img.save("circle.png")
