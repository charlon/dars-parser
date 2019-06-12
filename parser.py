from bs4 import BeautifulSoup


def parse(filepath):
    """ Parses an html DARS audit.
    """
    with open(filepath) as fp:
        myfile = fp.read()

    soup = BeautifulSoup(myfile, 'html.parser')

    return soup


if __name__ == "__main__":
    filepath = 'degrees/BS Aeronautical Astro Eng.html'
    soup = parse(filepath)
    print(soup.prettify())
