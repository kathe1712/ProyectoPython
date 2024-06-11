import pandas as pd
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time} seconds")
        return result
    return wrapper

@timer
def analyze_data(data):
    df = pd.DataFrame(data)
    df['price'] = df['price'].str.replace('$', '').astype(float)
    summary = df.describe()
    return summary

def save_to_csv(data, filename='data/products.csv'):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

def load_from_csv(filename='data/products.csv'):
    return pd.read_csv(filename)
