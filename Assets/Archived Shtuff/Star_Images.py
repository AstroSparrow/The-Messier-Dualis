from PIL import Image, ImageDraw
import random

# Image size
W, H = 1920, 1080

def make_layer(num_stars, min_r, max_r, filename):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    for _ in range(num_stars):
        x = random.randint(0, W-1)
        y = random.randint(0, H-1)
        r = random.randint(min_r, max_r)
        # white star with some random alpha
        alpha = random.randint(120, 255)
        draw.ellipse((x-r, y-r, x+r, y+r), fill=(255, 255, 255, alpha))
    img.save(f"Assets/Image Files/{filename}", "PNG")

make_layer(900, 1, 1, "stars_far.png")
make_layer(400, 1, 2, "stars_mid.png")
make_layer(120, 2, 3, "stars_near.png")