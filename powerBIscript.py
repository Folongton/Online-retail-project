import pandas as pd
import numpy as np

FILE_PATH = r'C:\Users\Vasyl\Desktop\Online retail project\data\Online Retail.xlsx'

df = pd.read_excel(FILE_PATH)
df['Cancelled'] = np.where(df['InvoiceNo'].astype(str).str.startswith('C'), 1, 0)

df = df.drop_duplicates()