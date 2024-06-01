# -*- coding:utf-8 -*-

from PIL import Image, ImageDraw, ImageFont, ImageOps

ImageFont.load_default()

font_choice = 7
if font_choice == 1:
    project_font = "font/Architects_Daughter/ArchitectsDaughter-Regular.ttf"
elif font_choice == 2:
    project_font = "font/Inconsolata/static/Inconsolata-SemiBold.ttf"
# elif font_choice == 3:
#     project_font = "font/Comfortaa/static/Comfortaa-Light.ttf"
elif font_choice == 4:
    project_font = "font/Open_Sans/OpenSans-SemiBold.ttf"
# elif font_choice == 5:
#     project_font = "font/Roboto/Roboto-Regular.ttf"
# elif font_choice == 6:
#     project_font = "font/Roboto_Slab/static/RobotoSlab-Regular.ttf"
# elif font_choice == 7:
#     project_font = "font/Ubuntu_Mono/UbuntuMono-Bold.ttf"
else:
    project_font = "font/Open_Sans/OpenSans-SemiBold.ttf"

font8 = ImageFont.truetype(project_font, 8)
font12 = ImageFont.truetype(project_font, 12)
font14 = ImageFont.truetype(project_font, 14)
font16 = ImageFont.truetype(project_font, 16)
font24 = ImageFont.truetype(project_font, 24)
font48 = ImageFont.truetype(project_font, 48)


class Display:
    def __init__(self):
        self.im_black = Image.new('1', (800, 480), 255)
        self.im_red = Image.new('1', (800, 480), 255)
        self.draw_black = ImageDraw.Draw(self.im_black)
        self.draw_red = ImageDraw.Draw(self.im_red)

    def draw_circle(self, x, y, r, c):
        if c == "b":
            self.draw_black.ellipse((x - r, y - r, x + r, y + r), fill=0)
        else:
            self.draw_red.ellipse((x - r, y - r, x + r, y + r), fill=0)

    def draw_icon(self, x, y, c, l, h, icon):
        im_icon = Image.open(f"icons/{icon}.png")
        # im_icon = im_icon.convert("LA")
        im_icon = im_icon.resize((l, h))
        if c == "b":
            self.im_black.paste(im_icon, (x, y), im_icon)
        else:
            self.im_red.paste(im_icon, (x, y), im_icon)

    def draw_image(self, x, y, l, h, image):
        image = Image.open(f"photo/{image}.png")
        image = image.resize((l, h))
                # Create masks for black and red
        image_rgb = image.convert('RGB')

        # Create black and red masks based on RGB values
        mask_black = Image.new('1', image_rgb.size, 1)  # Start with a white mask
        mask_red = Image.new('1', image_rgb.size, 1)    # Start with a white mask
        pixels = image_rgb.load()

        for i in range(image_rgb.width):
            for j in range(image_rgb.height):
                r, g, b = pixels[i, j]
                if r < 128 and g < 128 and b < 128:
                    mask_black.putpixel((i, j), 0)  # Black part
                elif r > 127 and g < 128 and b < 128:
                    mask_red.putpixel((i, j), 0)  # Red part

        # Convert the image to black and white and paste it
        image_bw = image.convert('1')
        self.im_black.paste(image_bw, (x, y), mask_black)
        self.im_red.paste(image_bw, (x, y), mask_red)

