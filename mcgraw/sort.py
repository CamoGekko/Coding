from bs4 import BeautifulSoup

html = """

"""

soup = BeautifulSoup(html, 'html.parser')

# Find all paragraphs and extract text
paragraphs = soup.find_all('p')
for p in paragraphs:
    print(p.get_text())
