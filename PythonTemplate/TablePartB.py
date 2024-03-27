import happybase as hb

# Establish a connection to HBase
connection = hb.Connection("localhost")

# Get the list of all tables
tables = connection.tables()

print(tables)
