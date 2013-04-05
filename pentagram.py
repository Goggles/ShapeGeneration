from PIL import Image, ImageDraw

size = (100, 100) 
img = Image.new('RGB', size)
draw = ImageDraw.Draw(img)

lines = [(0, 40), (100, 40), (0, 100), (50, 0), (100, 100), (0, 40)]

draw.polygon(lines, outline="red")

img.save("pentagram.png")
