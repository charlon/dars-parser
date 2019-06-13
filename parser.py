from bs4 import BeautifulSoup


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
    #import pdb; pdb.set_trace()
    print(soup.div.div.div['data-dprog'])
    print(soup.h1.string)
