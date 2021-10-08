import mysql.connector

# Mengkoneksikan MySQL ke Python
# Pastikan MySQL sudah terinstall dengan benar

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="q12we3"
)
print(mydb)

mycursor = mydb.cursor()

# Menampilkan Seluruh Database yang ada
mycursor.execute("Show Databases")
print(mycursor)
for db in mycursor:
  print(db)

# print("============")
# # Membuat Database
# mycursor.execute("CREATE DATABASE struktur_data")
# # mycursor.execute("DROP DATABASE struktur_data_2")

# mycursor.execute("Show Databases")
# for db in mycursor:
#   print(db)

