import happybase as hb

# DON'T CHANGE THE PRINT FORMAT, WHICH IS THE OUTPUT
# OR YOU WON'T RECEIVE POINTS FROM THE GRADER

# 1. update the data in a particular cell using the put() method
# 2. retrieve all versions of all columns, with the most recent version coming first

connection = hb.Connection("localhost")

table = connection.table("powers")

table.put(b"row7", {b"custom:color": b"purple"})

row = table.row(b"row7")
for key, value in row.items():
    cells = table.cells(b"row7", key, include_timestamp=True, versions=2)
    for name, time in cells:
        print(
            "row: {}, column family:qualifier: {}, value: {}, timestamp: {}".format(
                b"row7", key, name, time
            )
        )
