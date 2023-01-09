# Retrieve from page source strings that are defined by '[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]',
# Then pull out the middle letter from each string.
# url = 'http://www.pythonchallenge.com/pc/def/equality.html'

import re
import webbrowser
from evyatar_python_challenge.page_source import PageSource
from evyatar_python_challenge.split_data import SplitData


def find_letter_use_re(page_source_split):
    filter = '[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]'
    all = re.findall(filter, page_source_split)
    sol = ''.join(i[len(i)//2] for i in all)
    return sol


def replace_url(url, old_url, url_to_replace):
    new_url = url.replace(old_url, url_to_replace)
    webbrowser.open(new_url)
    return new_url


if __name__ == "__main__":
    url = 'http://www.pythonchallenge.com/pc/def/equality.html'
    page_source = PageSource(url).get_text()
    start = '<!--\n'
    end = '\n-->'
    page_source_split = SplitData(page_source, start=start, end=end).return_split_data()[-1]
    print(page_source_split)
    sol = find_letter_use_re(page_source_split)
    new_url = replace_url(url, 'equality.html', f'{sol}.html')
    print(new_url)