# url = 'http://www.pythonchallenge.com/pc/def/integrity.html'
# need to find a username and password that are in the page source and come as bits and convert them.

import bz2
from evyatar_python_challenge.page_source import PageSource
from evyatar_python_challenge.split_data import SplitData


def split_page_source(page_source):
    # splitA = page_source.split('<!--')
    # splitB = splitA[-1].split('-->')
    # splitC = splitB[0].split('\n')
    # print(page_source)
    # d = eval(str(page_source)
    split_page_source = page_source.split(r'\n')
    # print(a)
    un, pw = page_source.split(r'\n')[1][5:], page_source.split(r'\n')[2][5:]
    print(1, un)
    print(2, un.encode('latin1'))
    print(3, un.encode('latin1').decode('unicode_escape'))
    un = un.encode('latin1').decode('unicode_escape').encode('latin1')
    print(un)
    sol_un = bz2.decompress(un)
    print(sol_un)

    # print(d)
    # splitC = eval(page_source).split('\n')
    # print(len(splitC), splitC)
    #
    # un = split_page_source[1][5:-1].encode('latin1').decode('unicode_escape').encode('latin1')
    # pw = split_page_source[2][5:-1].encode('latin1').decode('unicode_escape').encode('latin1')
    return un, pw


def solution(un, pw):
    sol_un = bz2.decompress(un)
    sol_pw = bz2.decompress(pw)
    return sol_un, sol_pw


if __name__ == "__main__":
    url = 'http://www.pythonchallenge.com/pc/def/integrity.html'
    page_source = PageSource(url).get_text()
    start = '<!--'
    end = '-->'
    page_source_split = SplitData(page_source, start=start, end=end).return_split_data()
    print(page_source_split, len(page_source_split))
    un, pw = split_page_source(page_source_split)
    # sol_un, sol_pw = solution(un, pw)
    # print(sol_un, sol_pw)
