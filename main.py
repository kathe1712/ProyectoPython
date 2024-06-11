from scraping.scraper import get_product_data_bestbuy, save_to_csv
from analysis.analyzer import load_from_csv, analyze_data
from reports.reporter import generate_report
import time
import random

def main():
    # URLs de las tiendas en línea
    urls = [
        'https://www.bestbuy.com/site/searchpage.jsp?st=laptop',
        'https://www.bestbuy.com/site/searchpage.jsp?st=smartphone'
    ]
    
    all_products = []

    # Imprime los datos antes de la extracción
    print("Datos antes de la extracción:")
    print(all_products)

    # Extracción de datos de cada tienda
    for url in urls:
        print(f"Scraping data from {url}...")
        products = get_product_data_bestbuy(url)
        print(f"Products extracted: {products}")
        all_products.extend(products)
        time.sleep(random.uniform(1, 3))  # Añadir un retraso aleatorio entre 1 y 3 segundos

    # Imprime los datos después de la extracción
    print("Datos después de la extracción:")
    print(all_products)

    # Guardar los datos en un archivo CSV
    save_to_csv(all_products, 'bestbuy_products.csv')

    # Cargar los datos desde el archivo CSV
    loaded_data = load_from_csv()

    # Análisis de datos
    summary = analyze_data(loaded_data)
    print("Analysis Summary:")
    print(summary)

    # Generación de reporte en Excel
    generate_report(loaded_data)

if __name__ == "__main__":
    main()
