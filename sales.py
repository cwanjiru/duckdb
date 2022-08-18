import duckdb

conn = duckdb.connect("sales.duckdb")
cursor = conn.cursor()


query = "select transactionDate,product,prize.city,country"
print(cursor.execute(query).fetchdf())