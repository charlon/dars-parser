from bs4 import BeautifulSoup


def parse(filepath):

    with open(filepath) as fp:
        myfile = fp.read()

    soup = BeautifulSoup(myfile, 'html.parser')

    print(soup.prettify())


if __name__ == "__main__":
    filepath = 'degrees/BS Aeronautical Astro Eng.html'
    parse(filepath)
