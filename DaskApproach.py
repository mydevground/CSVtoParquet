##Dask approach
import dask.dataframe as dd
df = dd.read_csv('myInput.csv')
df.to_parquet('myOutput.parquet')