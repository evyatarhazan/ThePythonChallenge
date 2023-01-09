# url = 'http://www.pythonchallenge.com/pc/def/oxygen.html'
# Take the pixels of the image to reduce duplicates and convert the numbers to characters,
# and do it again on the numbers in the result.

import re
from PIL import Image
from evyatar_python_challenge.page_source import PageSource



def get_image_pixel(data):
    im = Image.open(data)
    pixel = list(im.getdata())
    width, height = im.size
    pixels = [pixel[i * width:(i + 1) * width] for i in range(height)]
    return pixels[47]


def get_single(pixels):
    item = [pixel[0] for pixel in pixels if pixel[0] == pixel[1] and pixel[0] == pixel[2]]
    new_list = []
    cuont = 0
    for i in range(len(item)):
        if item[i] == item[i-1]:
            cuont += 1
        else:
            if cuont > 6:
                new_list.append(item[i-1])
                new_list.append(item[i-1])
                cuont = 0
            else:
                new_list.append(item[i-1])
                cuont = 0
    new_list.append(new_list.pop(0))
    return new_list


def replace_to_chr(list_):
    string = ''
    for i in list_:
        string += chr(i)
    return string


def solution(chr_str):
    list_ = re.findall('[0-9]+', chr_str)
    for i in range(len(list_)):
        list_[i] = int(list_[i])
    sol = replace_to_chr(list_)
    return sol


def new_url(url, old_url, new_url):
    new_url = url.replace(old_url, new_url)
    return new_url


if __name__ == "__main__":
    url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
    page_source = PageSource(url, stream=True).get_raw()
    pixels = get_image_pixel(page_source)
    single = get_single(pixels)
    chr_str = replace_to_chr(single)
    print(chr_str)
    sol = solution(chr_str)
    print(sol)
    new_url = new_url(url, 'oxygen.png', f'{sol}.html')
    print(new_url)


