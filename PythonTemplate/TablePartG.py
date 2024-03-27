import happybase as hb

# DON'T CHANGE THE PRINT FORMAT, WHICH IS THE OUTPUT
# OR YOU WON'T RECEIVE POINTS FROM THE GRADER

connection = hb.Connection("localhost")
table = connection.table("powers")

rows = [row for row in table.scan()]

for key, data in rows:
    color = data[b"custom:color"]
    name = data[b"professional:name"]
    power = data[b"personal:power"]
    for key1, data1 in rows:
        color1 = data1[b"custom:color"]
        name1 = data1[b"professional:name"]
        power1 = data1[b"personal:power"]

        if color == color1 and name != name1:
            print("{}, {}, {}, {}, {}".format(name, power, name1, power1, color))
