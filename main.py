from scraping.scraper import get_product_data, save_to_csv
import time
import random

def main():
    # URL del sitio web de prueba
    url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers'
    
    all_products = []

    # Imprime los datos antes de la extracción
    print("Datos antes de la extracción:")
    print(all_products)

    # Extracción de datos de la tienda
    print(f"Scraping data from {url}...")
    products = get_product_data(url)
    print(f"Products extracted: {products}")
    all_products.extend(products)
    time.sleep(random.uniform(1, 3))  # Añadir un retraso aleatorio entre 1 y 3 segundos

    # Imprime los datos después de la extracción
    print("Datos después de la extracción:")
    print(all_products)

    # Guardar los datos en un archivo CSV
    save_to_csv(all_products, 'products.csv')

if __name__ == "__main__":
    main()
