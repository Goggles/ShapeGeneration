from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGBA', (100, 100), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSansBold.ttf", 10)


draw.text((10, 50), "Hello World!", font=font, fill="green")

img.save("text.png")
