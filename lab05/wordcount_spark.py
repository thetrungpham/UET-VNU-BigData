from pyspark.sql import SparkSession

# Khởi tạo SparkSession
spark = SparkSession.builder.appName("WordCountExample").getOrCreate()
sc = spark.sparkContext

# Đọc file text
text_file = sc.textFile("hdfs:///input/some_words.txt")

# Word count
counts = (text_file
          .flatMap(lambda line: line.split(" "))
          .map(lambda word: (word, 1))
          .reduceByKey(lambda a, b: a + b))

# Hiển thị kết quả
for word, count in counts.collect():
    print(f"{word}: {count}")

counts.saveAsTextFile("hdfs:///output")
# Dừng Spark
spark.stop()



