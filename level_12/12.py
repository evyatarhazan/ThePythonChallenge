#3 url = 'http://www.pythonchallenge.com/pc/return/evil.html'

import webbrowser
from evyatar_python_challenge.page_source import PageSource


def division_into_five(data):
    five_part = []
    for i in range(5):
        five_part.append(data[i::5])
    return five_part


def create_image(list_image):
    for i in range(len(list_image)):
        open(f'{i}.jpg', 'wb').write(list_image[i])
    return 'disproportional'


def replace_url(url, old_url, url_to_replace):
    new_url = url.replace(old_url, url_to_replace)
    webbrowser.open(new_url)
    return new_url


if __name__ == '__main__':
    url = 'http://www.pythonchallenge.com/pc/return/evil2.gfx'
    user = 'huge'
    password = "file"
    page_source = PageSource(url, user=user, password=password).get_content()
    division_into_five = division_into_five(page_source)
    create_image = create_image(division_into_five)
    new_url = replace_url(url, 'evil2.gfx', f'{create_image}.html')
    print(new_url)