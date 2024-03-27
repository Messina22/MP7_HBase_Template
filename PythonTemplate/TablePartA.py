import happybase as hb

# Establish a connection to HBase
connection = hb.Connection("localhost")

# Create the 'powers' table with 'personal', 'professional', and 'custom' column families
connection.create_table(
    "powers", {"personal": dict(), "professional": dict(), "custom": dict()}
)

# Create the 'food' table with 'nutrition' and 'taste' column families
connection.create_table("food", {"nutrition": dict(), "taste": dict()})
