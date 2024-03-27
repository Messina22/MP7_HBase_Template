import happybase as hb

# DON'T CHANGE THE PRINT FORMAT, WHICH IS THE OUTPUT
# OR YOU WON'T RECEIVE POINTS FROM THE GRADER

connection = hb.Connection("localhost")
table = connection.table("powers")

# rows = table.scan()
# for key, data in rows:
#     print(key, data)

data = table.row(
    b"row1",
    columns=[
        "personal:hero",
        "personal:power",
        "professional:name",
        "professional:xp",
        "custom:color",
    ],
)
hero = data[b"personal:hero"]
power = data[b"personal:power"]
name = data[b"professional:name"]
xp = data[b"professional:xp"]
color = data[b"custom:color"]

print(
    "hero: {}, power: {}, name: {}, xp: {}, color: {}".format(
        hero, power, name, xp, color
    )
)

data = table.row(
    b"row19",
    columns=[
        "personal:hero",
        "custom:color",
    ],
)
hero = data[b"personal:hero"]
color = data[b"custom:color"]

print("hero: {}, color: {}".format(hero, color))

data = table.row(
    b"row1",
    columns=[
        "personal:hero",
        "professional:name",
        "custom:color",
    ],
)
hero = data[b"personal:hero"]
name = data[b"professional:name"]
color = data[b"custom:color"]
print("hero: {}, name: {}, color: {}".format(hero, name, color))
