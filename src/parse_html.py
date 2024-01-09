from bs4 import BeautifulSoup

with open('../data/posters.html', 'r', encoding='utf8') as f:
    html_content = f.read()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract titles and abstracts
poster_divs = soup.find_all('div', class_='displaycards touchup-date')

print(f"{len(poster_divs) = }")

for poster_div in poster_divs[:3]:
    title = poster_div.find('a', class_='small-title').text.strip()
    title = title.replace('\n', '')
    title = ' '.join(title.split())

    abstract_link = poster_div.find('a', class_='abstract-link')
    abstract_id = abstract_link['id'].split('-')[-1]
    abstract_collapse_id = f"collapse-event-abstract-{abstract_id}"
    abstract_div = soup.find('div', id=abstract_collapse_id)
    try:
        abstract_text = abstract_div.find('div', class_='abstract-display').find('p').text.strip()
        abstract_text = abstract_text.replace('\n', '')
        abstract_text = ' '.join(abstract_text.split())
    # no abstract
    except AttributeError:
        abstract_text = ''

    print(f"Title: {title}")
    print(f"Abstract: {abstract_text}")
    print("----")
