#pyspark approach
from pyspark.sql import SparkSession
spark = SparkSession.builder \
  .master("local") \
  .appName("parquet_example") \
  .getOrCreate()
df = spark.read.csv('myInput.csv', header = True)
df.repartition(1).write.mode('overwrite').parquet('myOutput.parquet')