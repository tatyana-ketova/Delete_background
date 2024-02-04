from PIL import Image


def remove_back(image_obj,threshold):
    image = Image.open(image_obj.image)
    image = image.convert('RGBA')
    pixels = image.load()
    for y in range(image.size[1]):
        for x in range(image.size[0]):
            pixel_color = pixels[x, y][:3]
            if all(abs(c - 255) < threshold for c in pixel_color):
                pixels[x, y] = (0, 0, 0, 0)

    return image


