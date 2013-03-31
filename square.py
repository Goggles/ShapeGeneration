from PIL import Image, ImageDraw

size = (100, 100)
img = Image.new('RGB', size)
draw = ImageDraw.Draw(img)

draw.rectangle((10, 10, 90, 90), fill="yellow", outline="red")


img.save("square.png")
