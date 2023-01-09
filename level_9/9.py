# url = 'http://www.pythonchallenge.com/pc/return/good.html'
# You need to create an image and color the existing coordinates in page source accordingly
import requests
from requests.auth import HTTPBasicAuth
import re
from PIL import Image, ImageDraw

from evyatar_python_challenge.page_source import PageSource


def get_page_source(url):
    user = 'huge'
    password = "file"
    res = requests.get(url, auth=HTTPBasicAuth(user, password))
    return res.text


def split_page_source(page_source):
    splitA = page_source.split('first:')[-1]
    splitB = splitA.split('second:')
    first_str = re.findall('[0-9]+', splitB[0])
    second_str = re.findall('[0-9]+', splitB[1])
    first = [int(i) for i in first_str]
    second = [int(i) for i in second_str]

    return first, second


def solution(fisrt, second):
    size = 0
    for i in fisrt:
        if i > size:
            size = i

    img = Image.new('RGB', (size+50, size+50), color=(0, 255, 255))
    d = ImageDraw.Draw(img)
    d.polygon(first, fill=(255, 0, 255))
    d.polygon(second, fill=(255, 255, 0))
    img.show()
    return 'bull'


def replace_url(url, old_url, new_url):
    new_url = url.replace(old_url, new_url)
    return new_url


if __name__ == '__main__':
    url = 'http://www.pythonchallenge.com/pc/return/good.html'
    user = 'huge'
    password = "file"
    page_source = PageSource(url, user=user, password=password).get_text()
    first, second = split_page_source(page_source)
    sol = solution(first, second)
    new_url = replace_url(url, 'good.html', f'{sol}.html')
    print(new_url)

