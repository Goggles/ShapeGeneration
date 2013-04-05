from PIL import Image, ImageDraw

size = (100, 100) 
img = Image.new('RGB', size)
draw = ImageDraw.Draw(img)

lines = [(50, 0), (100, 100), (0, 100)]

draw.polygon(lines, fill="red")

img.save("triangle.png")
