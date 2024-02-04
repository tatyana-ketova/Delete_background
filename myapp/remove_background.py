from PIL import Image


def remove_back(image_obj,threshold):
    # Open the image file using Pillow's 'Image.open()' function.
    image = Image.open(image_obj.image)
    # Convert the image to the RGBA color mode to allow manipulation of alpha channel (transparency).
    image = image.convert('RGBA')
    # Load the pixel data of the image.
    pixels = image.load()
    # Iterate over each pixel in the image.
    for y in range(image.size[1]):
        for x in range(image.size[0]):
            # Get the RGB color of the current pixel.
            pixel_color = pixels[x, y][:3]
            # Check if the pixel color is close to white based on the threshold value.
            if all(abs(c - 255) < threshold for c in pixel_color):
                # Set the alpha channel of the pixel to 0 (transparent) if the pixel color is close to white.
                pixels[x, y] = (0, 0, 0, 0)
    # Return the modified image after background removal.
    return image


