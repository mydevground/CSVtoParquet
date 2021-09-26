##Pandas approach
import pandas as pd
df = pd.read_csv('myInput.csv')
df.to_parquet('myOutput.parquet')