# Replace each letter with the letter that comes after two letters in alphabetical order
# url = http://www.pythonchallenge.com/pc/def/map.html

import webbrowser
from evyatar_python_challenge.page_source import PageSource
from evyatar_python_challenge.split_data import SplitData


# My_solution
def My_solution(data):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    letter_dict = {}
    for i in range(len(letters)-2):
        letter_dict[letters[i]] = letters[i+2]
    letter_dict[letters[-1]] = letters[1]
    letter_dict[letters[-2]] = letters[0]
    new_data = ''
    for i in data:
        if i in letter_dict:
            new_data += letter_dict[i]
        else:
            new_data += i
    return new_data


# their_solution
def maketrans_data(data):
    old_letters = 'abcdefghijklmnopqrstuvwxyz'
    new_letters = old_letters[2:]+old_letters[0:2]
    new_data = data.maketrans(old_letters, new_letters)
    new_data_translate = data.translate(new_data)
    return new_data_translate


def replace_url(url, old_url, url_to_replace):
    new_url = url.replace(old_url, url_to_replace)
    webbrowser.open(new_url)
    return new_url


if __name__ == "__main__":
    url = 'http://www.pythonchallenge.com/pc/def/map.html'
    page_source = PageSource(url).get_text()
    start = '<font color="#f000f0">\n'
    end = '\n</tr></td>'
    split_page_source = SplitData(page_source, start=start, end=end).return_split_data()
    print(split_page_source)
    sol = My_solution(split_page_source)
    old_url = 'map'
    print(sol)
    url_sol = maketrans_data('map')
    print(url_sol)
    new_url = replace_url(url, old_url, url_sol)
    print(new_url)


