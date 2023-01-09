# url = 'http://www.pythonchallenge.com/pc/return/bull.html'
import re


def look_and_Say_Sequence_recursion(n, num_str='1'):
    if n == 1 or n == 0:
        return num_str
    else:
        element = '$'
        new_num = ''
        count = 0
        for i in num_str:
            if i != element:
                new_num += str(count)
                new_num += element
                element = i
                count = 1
            else:
                count += 1
        new_num += str(count)
        new_num += element
        return look_and_Say_Sequence_recursion(n - 1, new_num[2:])


def look_and_Say_Sequence_while(n, num_str='1'):
    while n != 0:
        re_list = re.findall('[1]+|[2]+|[3]+', num_str)
        new_num = ''.join(str(len(i)) + i[0] for i in re_list)
        num_str = new_num
        n -= 1
    return len(num_str)


def sol_in_one_line(n, num_str='1'):
    for j in range(n):
        num_str = ''.join(str(len(i)) + i[0] for i in re.findall('[1]+|[2]+|[3]+', num_str))
    return len(num_str)


def replace_url(url, old_url, new_url):
    new_url = url.replace(old_url, new_url)
    return new_url


if __name__ == '__main__':
    url = 'http://www.pythonchallenge.com/pc/return/bull.html'
    sol_recursion = look_and_Say_Sequence_recursion(31)
    new_url = replace_url(url, 'bull', str(len(sol_recursion)))
    # print(new_url)
    sol_while = look_and_Say_Sequence_while(30)
    new_url = replace_url(url, 'bull', str(sol_while))
    # print(new_url)
    sol_while = sol_in_one_line(30)
    print(sol_while)
    new_url = replace_url(url, 'bull', str(sol_while))
    print(new_url)
