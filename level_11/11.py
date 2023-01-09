# url = 'http://www.pythonchallenge.com/pc/return/5808.html'


import numpy as np
from PIL import Image
from evyatar_python_challenge.page_source import PageSource



def get_image_pixel(page_source):
    im = Image.open(page_source)
    im.show()
    pixel = list(im.getdata())
    width, height = im.size
    pixels = [pixel[i * width:(i + 1) * width] for i in range(height)]
    return pixels


def image_processing(pixels):
    new_pixel = []
    for line in range(1, len(pixels), +2):
            new_line = []
            for pixel_in_line in range(1, len(pixels[line]), +2):
                new_line.append(pixels[line][pixel_in_line])
            new_pixel.append(new_line)
    return new_pixel


def show_new_image(new_pixels):
    array = np.array(new_pixels, dtype=np.uint8)
    new_image = Image.fromarray(array)
    new_image.show()
    return 'evil'


def replace_url(url, old_url, new_url):
    new_url = url.replace(old_url, new_url)
    return new_url


if __name__ == '__main__':
    url = 'http://www.pythonchallenge.com/pc/return/cave.jpg'
    user = 'huge'
    password = "file"
    page_source = PageSource(url, stream=True, user=user, password=password).get_raw()
    pixels = get_image_pixel(page_source)
    new_pixel = image_processing(pixels)
    sol = show_new_image(new_pixel)
    new_url = replace_url(url, 'cave.jpg', f'{sol}.html')
    print(new_url)