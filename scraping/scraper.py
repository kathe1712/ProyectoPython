import requests
from bs4 import BeautifulSoup
import random
import csv

# Lista de User-Agents para rotar
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.3',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.3',
]

def get_product_data(url):
    headers = {
        'User-Agent': random.choice(user_agents)
    }
    
    try:
        response = requests.get(url, headers=headers)
        print(f"Request to {url} returned status code {response.status_code}")
        
        if response.status_code != 200:
            print(f"Error: Status code {response.status_code}")
            return []

        soup = BeautifulSoup(response.content, 'html.parser')
        print("Successfully parsed HTML content with BeautifulSoup")

        products = []
        items = soup.find_all('div', class_='product-wrapper card-body')

        print(f"Found {len(items)} items on the page.")

        for item in items:
            name_tag = item.find('a', class_='title')
            price_tag = item.find('h4', class_='price')

            if name_tag and price_tag:
                name = name_tag['title'].strip()
                price = price_tag.text.strip().replace('$', '')
                products.append({
                    'name': name,
                    'price': price
                })
            else:
                print("Missing name or price tag in item:")
                print(item.prettify())

        return products
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return []

def save_to_csv(products, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'price'])
        writer.writeheader()
        writer.writerows(products)
