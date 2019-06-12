from bs4 import BeautifulSoup


def main():
    filepath = 'degrees/BS Aeronautical Astro Eng.html'

    with open(filepath) as fp:
        myfile = fp.read()

    soup = BeautifulSoup(myfile, 'html.parser')

    print(soup.prettify())


if __name__ == "__main__":
    main()
