# url = 'http://www.pythonchallenge.com/pc/def/channel.html'
# You get a ZIP file that contains a linked list of files.
# You need to go through the linked list and take the comment of each file and then convert from bytes to str ('utf-8').

import zipfile, io
import re
import os
from evyatar_python_challenge.page_source import PageSource



def open_zip_file(zip_file):
    z = zipfile.ZipFile(io.BytesIO(zip_file))
    z.extractall()
    return ['readme.txt', z]


def solution(name_file, z):
    comment = ''
    number = 'a'
    while len(number) != 0:
        comment += z.getinfo(name_file).comment.decode("utf-8")
        file = open(name_file, 'r').read()
        f = re.findall(' [0-9]+', file)
        if len(f) == 0:
            break
        number = re.findall('[0-9]+', f[0])
        os.remove(name_file)
        name_file = f'{number[0]}.txt'
    os.remove(name_file)
    return comment


def find_new_url(data):
    new_url = re.findall('[A-Z]', data)
    new_url_str = ''
    for i in new_url:
        if i not in new_url_str:
            new_url_str += i
    return new_url_str.lower()


def new_url(url, old_url, new_url):
    new_url = url.replace(old_url, new_url)
    return new_url


if __name__ == "__main__":
    url = 'http://www.pythonchallenge.com/pc/def/channel.zip'
    page_source = PageSource(url).get_content()
    open_zip_file = open_zip_file(page_source)
    sol = solution(open_zip_file[0], open_zip_file[1])
    print(sol)
    find_new_url = find_new_url(sol)
    new_url = new_url(url, 'channel.zip', f'{find_new_url}.html')
    print(new_url)



