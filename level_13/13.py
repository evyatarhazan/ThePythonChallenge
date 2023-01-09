import urllib.request

import requests
from requests.auth import HTTPBasicAuth


def get_page_source(url):
    user = 'huge'
    password = "file"
    res = requests.get(url, auth=HTTPBasicAuth(user, password)).text
    return res



if __name__ == '__main__':
    url = 'http://www.pythonchallenge.com/pc/return/disproportional.html'
    page_source = get_page_source(url)
    print(page_source)
    url = 'http://www.pythonchallenge.com/pc/phonebook.php'
    page_source = get_page_source(url)
    print(page_source)