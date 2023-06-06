import mysql.connector

# Connect to the MySQL server
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="inatel"
)

# Create a cursor to execute SQL queries
cursor = cnx.cursor()

# Insert two rows into the wifi_data table
insert_query = "INSERT INTO wifi_data (device_id, bssid, rssi) VALUES (%s, %s, %s)"

data = [
    (1, "BSSID1", -70),
    (2, "BSSID2", -80)
]

cursor.executemany(insert_query, data)

# Commit the changes to the database
cnx.commit()

# Close the cursor and the connection
cursor.close()
cnx.close()
