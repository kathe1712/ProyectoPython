import requests
from bs4 import BeautifulSoup
import random
import csv
import time

# Lista de User-Agents para rotar
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.3',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.3',
]

def get_product_data_bestbuy(url):
    headers = {
        'User-Agent': random.choice(user_agents)
    }
    
    try:
        # Realizar la solicitud HTTP con los encabezados y llamar a end_headers()
        request = requests.Request('GET', url, headers=headers)
        prepared_request = request.prepare()
        prepared_request.headers['User-Agent'] = random.choice(user_agents)
        session = requests.Session()
        response = session.send(prepared_request)
        response.raise_for_status()
        response.end_headers()  # Llamar explícitamente a end_headers()

        print(f"Request to {url} returned status code {response.status_code}")
        
        if response.status_code != 200:
            print(f"Error: Status code {response.status_code}")
            return []

        soup = BeautifulSoup(response.content, 'html.parser')
        print("Successfully parsed HTML content with BeautifulSoup")

        products = []
        items = soup.find_all('li', {'class': 'sku-item'})

        print(f"Found {len(items)} items on BestBuy page.")

        for item in items:
            name_tag = item.find('h4', {'class': 'sku-title'})
            price_tag = item.find('span', {'class': 'sr-only'})

            if name_tag and price_tag:
                name = name_tag.text.strip()
                price = price_tag.text.split('$')[1].strip()
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


