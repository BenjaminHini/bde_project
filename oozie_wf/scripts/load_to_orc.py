from pyhive import hive
import json

# Connect to Hive
# conn = hive.Connection(host='<hostname>', port=<port>, username='<username>')
# cursor = conn.cursor()

# Read data from JSON file
with open('daily_scrap.json', 'r') as f:
    data = json.load(f)

# Insert data into ORC table
for i in range(12):
    date = data["dates"][str(i)]
    sign = data["signs"][str(i)]
    desc = data["description"][str(i)]
    # cursor.execute("INSERT INTO <orc_table> VALUES (%s, %s, %s)", row)

# Commit the transaction
# conn.commit()

# Close the connection
# conn.close()
