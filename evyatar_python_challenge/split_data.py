import re

# print(re.search("<!--(.*)-->", s).group(1))

class SplitData:
    def __init__(self, data, start, end):
        print(repr(data))
        self.data = re.search(f'{start}(.*){end}+', repr(data))
        # print(self.data.group(0))


    def return_split_data(self):
        return self.data.group(1)