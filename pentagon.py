from PIL import Image, ImageDraw

size = (100, 100) 
img = Image.new('RGB', size)
draw = ImageDraw.Draw(img)

lines = [(50, 0), (0, 40), (20, 100), (80, 100), (100, 40)]

draw.polygon(lines, fill="blue")

img.save("pentagon.png")
