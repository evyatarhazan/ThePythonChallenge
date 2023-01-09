# find rare characters in the page source
# url = 'http://www.pythonchallenge.com/pc/def/ocr.html'

import webbrowser
from evyatar_python_challenge.page_source import PageSource
from evyatar_python_challenge.split_data import SplitData



def create_Hash_table(page_source_split):
    dict_characters = {}
    for i in page_source_split:
        if i in dict_characters:
            dict_characters[i] += 1
        else:
            dict_characters[i] = 1
    return dict_characters


def find_rare_characters(dict_characters):
    min = 1
    rare_characters = ''
    while len(rare_characters) == 0:
        print(rare_characters)
        for i in dict_characters:
            if dict_characters[i] == min:
                rare_characters += i
        min += 1
    return rare_characters


def replace_url(url, old_url, url_to_replace):
    new_url = url.replace(old_url, url_to_replace)
    webbrowser.open(new_url)
    return new_url


if __name__ == "__main__":
    url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
    page_source = PageSource(url).get_text()
    start = '<!--\n'
    end = '\n-->'
    page_source_split = SplitData(page_source, start=start, end=end).return_split_data()[-1][6:-5]
    print(page_source_split)
    create_Hash_table = create_Hash_table(page_source_split)
    rare_characters = find_rare_characters(create_Hash_table)
    new_url = replace_url(url, 'ocr.html', f'{rare_characters}.html')
    print(new_url)
