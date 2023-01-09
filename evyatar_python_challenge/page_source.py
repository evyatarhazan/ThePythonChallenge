import requests
from requests.auth import HTTPBasicAuth


class PageSource:
    """
    Get the page source from url using method requests.get().

    ---
    Attributes
    ----------
    url : str
        url to get the page source from it

    Method's
    --------
    get_text()
        return requests.get().text
    get_content()
        return requests.get().content
    get_raw()
        return requests.get().raw

    for more information, go to the method's documentation of requests
    """

    def __init__(self, url, stream=None, user=None, password=None):
        """
        parameters
        ----------
        url : str
            url to get the page source from it
        stream : bool
            stream. by default : None
        user : str
            username for authentication. by default : None
        password : str
            password for authentication. by default : None
        """
        self.url = requests.get(url, stream=stream, auth=HTTPBasicAuth(user, password))

    def get_text(self):
        """
        return : requests.get().text
        """
        return self.url.text

    def get_content(self):
        """
        return : requests.get().content
        """
        return self.url.content

    def get_raw(self):
        """
        return : requests.get().raw
        """
        return self.url.raw

