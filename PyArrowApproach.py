##PyArrow approach
import pyarrow.csv as pv
import pyarrow.parquet as pq
table = pv.read_csv('myInput.csv')
pq.write_table(table, 'myOutput.parquet')