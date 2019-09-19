#! /usr/bin/env python3

from bs4 import BeautifulSoup


class DegreeRequirements:
    code = ''
    name = ''

    def __init__(self, soup):
        self.code = soup.div['data-dprog']
        self.name = soup.h1.string.lstrip(' ').rstrip(' ')

def parse(filepath):
    """ Parses an html DARS audit.
    """
    with open(filepath) as fp:
        myfile = fp.read()

    soup = BeautifulSoup(myfile, 'html.parser')

    return soup


if __name__ == "__main__":
    filepath = 'degrees/astronomy.html'
    soup = parse(filepath)
    curric = DegreeRequirements(soup)
    print(curric.code)
    print(curric.name)
