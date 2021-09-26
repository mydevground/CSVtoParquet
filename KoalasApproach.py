#koalas approach
import databricks.koalas as ks
df = ks.read_csv('myInput.csv')
df.to_parquet('myOutput.parquet')