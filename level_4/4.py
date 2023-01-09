# url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
# Listlinks: Go through each of the listlinks until you get the URL


import re
from evyatar_python_challenge.page_source import PageSource



def solution(url, number):
    page_source = PageSource(url+number[0]).get_text()
    print(page_source)
    string = re.findall('and the next nothing is [0-9]+', page_source)

    # Extreme case:
    if page_source == 'Yes. Divide by two and keep going.':
        number = [str(int(number[0])//2)]
        return solution(url, number)

    elif len(string) == 0:
        return page_source

    else:
        number = re.findall('[0-9]+', string[0])
        return solution(url, number)


def new_url(url, old_url, new_url):
    new_url = url.replace(old_url, new_url)
    return new_url


if __name__ == "__main__":
    number = ['12345']
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
    sol = solution(url + '?nothing=', number)
    new_url = new_url(url, 'linkedlist.php', sol)
    print(new_url)





