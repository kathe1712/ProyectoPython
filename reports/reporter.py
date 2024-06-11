import pandas as pd

def generate_report(data, filename='data/report.xlsx'):
    df = pd.DataFrame(data)
    with pd.ExcelWriter(filename) as writer:
        df.to_excel(writer, index=False, sheet_name='Products')
