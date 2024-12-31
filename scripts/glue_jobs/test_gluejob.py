from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Write Parquet to Glue Table").getOrCreate()
spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3.canned.acl", "BucketOwnerFullControl")
csv_file_path = "s3://test-bucket-536697232936-us-east-1"
df = spark.read.csv(csv_file_path, header=True, inferSchema=True)
df.show()
glue_database = "test_glue_database"  # Glue Database
glue_table = "test_glue_table"        # Glue Table
df.write \
    .format("parquet") \
    .option("database", glue_database) \
    .option("table", glue_table) \
    .option("path", "s3://test-bucket-536697232936-us-east-1/test_data") \
    .mode("overwrite") \
    .save()
spark.stop()

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Write Parquet to Glue Table").getOrCreate()
spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3.canned.acl", "BucketOwnerFullControl")
csv_file_path = "s3://test-bucket-536697232936-us-east-1/archive_IPL_Players/"
df = spark.read.csv(csv_file_path, header=True,inferSchema=True)
df.show()
glue_database = "test_glue_database"  # Glue Database
glue_table = "test_glue_table"        # Glue Table
df.write.options(path="s3://test-bucket-536697232936-us-east-1/test_data").format("parquet").mode("overwrite").saveAsTable(f"{glue_database}.{glue_table}")
spark.stop()

