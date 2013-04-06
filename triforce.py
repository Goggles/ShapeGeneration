from PIL import Image, ImageDraw

size = (100, 100) 
img = Image.new('RGB', size)
draw = ImageDraw.Draw(img)

courage = [(100, 100), (50, 100), (75, 50), (100, 100)]
wisdom = [(0, 100), (50, 100), (25, 50), (0, 100)]
power = [(50, 0), (75, 50), (25, 50), (50, 0)]


draw.polygon(courage, outline="green")
draw.polygon(wisdom, outline="blue")
draw.polygon(power, outline="red")

img.save("triforce.png")
