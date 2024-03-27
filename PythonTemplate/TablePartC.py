import happybase as hb
import csv

# Establish a connection to HBase
connection = hb.Connection("localhost")

# Get a reference to the 'powers' table
table = connection.table("powers")

# Open the CSV file
with open("input.csv", "r") as file:
    reader = csv.reader(file)

    # For each row in the CSV file
    for row in reader:
        # Insert the data into the 'powers' table
        table.put(
            str(row[0]).encode(),
            {
                b"personal:hero": str(row[1]).encode(),
                b"personal:power": str(row[2]).encode(),
                b"professional:name": str(row[3]).encode(),
                b"professional:xp": str(row[4]).encode(),
                b"custom:color": str(row[5]).encode(),
            },
        )
