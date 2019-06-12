from bs4 import BeautifulSoup


soup = BeautifulSoup('degrees/BS Aeronautical Astro Eng.html', 'html.parser')

print(soup.prettify())
