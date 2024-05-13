import requests
import json
from bs4 import BeautifulSoup
from pymongo import MongoClient


def scrape_quotes():
    base_url = "http://quotes.toscrape.com"
    quotes_data = []
    authors_data = []

    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for quote in soup.find_all('div', class_='quote'):
        quote_text = quote.find('span', class_='text').text.strip()
        author_name = quote.find('small', class_='author').text.strip()
        tags = [tag.text for tag in quote.find_all('a', class_='tag')]
        quotes_data.append({"quote": quote_text, "author": author_name, "tags": tags})

        if author_name not in [author['fullname'] for author in authors_data]:
            authors_data.append({"fullname": author_name})

    next_page = soup.find('li', class_='next')
    while next_page:
        next_page_url = base_url + next_page.a['href']
        response = requests.get(next_page_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        for quote in soup.find_all('div', class_='quote'):
            quote_text = quote.find('span', class_='text').text.strip()
            author_name = quote.find('small', class_='author').text.strip()
            tags = [tag.text for tag in quote.find_all('a', class_='tag')]
            quotes_data.append({"quote": quote_text, "author": author_name, "tags": tags})

            if author_name not in [author['fullname'] for author in authors_data]:
                authors_data.append({"fullname": author_name})

        next_page = soup.find('li', class_='next')

    return quotes_data, authors_data


def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)


def import_to_mongodb(data, collection_name):
    client = MongoClient("mongodb+srv://denluts33:PisiaSlona@denysluts.nr7rna0.mongodb.net/")
    db = client["<database>"]
    collection = db[collection_name]
    collection.insert_many(data)
    print(f"{len(data)} documents imported to {collection_name} collection.")


if __name__ == "__main__":
    quotes_data, authors_data = scrape_quotes()

    save_to_json(quotes_data, 'quotes.json')
    save_to_json(authors_data, 'authors.json')


    import_to_mongodb(quotes_data, 'quotes')
    import_to_mongodb(authors_data, 'authors')
