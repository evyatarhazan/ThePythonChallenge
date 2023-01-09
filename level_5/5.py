# url = 'http://www.pythonchallenge.com/pc/def/peak.html'
# U get data pickle and you need to open that with pickle method and parser that

import io
import pandas as pd
from evyatar_python_challenge.page_source import PageSource



def pickle_load(data):
    pickle_load = pd.read_pickle(io.BytesIO(data))
    return pickle_load


def solution(page_source):
    sol = ''
    for i in page_source:
        for j in i:
            sol += j[0] * j[1]
        sol += '\n'
    return sol


def new_url(url, old_url, new_url):
    new_url = url.replace(old_url, new_url)
    return new_url


if __name__ == "__main__":
    url = 'http://www.pythonchallenge.com/pc/def/banner.p'
    page_source = PageSource(url).get_content()
    pickle_load = pickle_load(page_source)
    sol = solution(pickle_load)
    print(sol)
    new_url = new_url(url, 'banner.p', 'channel.html')
    print(new_url)