import re
import webbrowser
import requests
from requests.auth import HTTPBasicAuth


def get_page_source(url):
    """
    get the page source from url address.
    ------

    :param url: str
    :return: page_source - str
    """
    user = 'huge'
    password = "file"
    page_source = requests.get(url, auth=HTTPBasicAuth(user, password)).text
    return page_source


def look_and_say_sequence(n, num_str='1'):
    """
    Constructs the look_and_say_sequence
    --------

    :param n: number
    :param num_str: str
    :return: the len of the organ n in series
    """
    for i in range(n):
        num_str = ''.join(str(len(j)) + j[0] for j in re.findall('[1]+|[2]+|[3]+', num_str))
    return len(num_str)


def replace_url(url, old_replace, new_replace):
    """

    :param url:
    :param old_replace:
    :param new_replace:
    :return:
    """
    new_url = url.replace(old_replace, new_replace)
    # webbrowser.open(new_url)
    return new_url


def main():
    """

    :return:
    """
    url = 'http://www.pythonchallenge.com/pc/return/bull.html'
    page_source = get_page_source(url)
    look_and_say_sequenc = look_and_say_sequence(30)
    new_url = replace_url(url, 'bull.html', f'{look_and_say_sequenc}.html')
    print(new_url)


if __name__ == '__main__':
    main()
