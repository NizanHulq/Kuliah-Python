import mysql.connector

# Mengkoneksikan MySQL ke Python
# Pastikan MySQL sudah terinstall dengan benar

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="q12we3",
  database="struktur_data"
)
print(mydb)

mycursor = mydb.cursor()

# Membuat Tabel Presensi
# mycursor.execute("CREATE TABLE presensi (nama VARCHAR(255), nim VARCHAR(255), kelas VARCHAR(255))")

mycursor.execute("SHOW TABLES")
# mycursor.execute("Show Databases")
for x in mycursor:
  print(x)

# Insert Data ke Tabel Presensi
# sql = "INSERT INTO presensi (nama, nim, kelas) VALUES (%s, %s, %s)"
# val = ("Alviska", "123", "A")
# mycursor.execute(sql, val)
# mydb.commit()
#
#
# # Insert Data ke Tabel Presensi
# sql = "INSERT INTO presensi (nama, nim, kelas) VALUES (%s, %s, %s)"
# val = ("Galuh", "456", "B")
# mycursor.execute(sql, val)
# mydb.commit()
#
#
# # Insert Data ke Tabel Presensi
# sql = "INSERT INTO presensi (nama, nim, kelas) VALUES (%s, %s, %s)"
# val = ("Nurwana", "789", "C")
# mycursor.execute(sql, val)
# mydb.commit()

# Menampilkan Data
# mycursor.execute("SELECT * FROM presensi")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

print("===============")

# Menghapus Data
# sql = "DELETE FROM presensi WHERE nim = '789'"
# mycursor.execute(sql)
# mydb.commit()

# Menampilkan Seluruh Data
# mycursor.execute("SELECT * FROM presensi")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

# Mengubah Data
# sql = "UPDATE presensi SET nama = 'Alviska Galuh Nurwana' WHERE kelas = 'A'"
# mycursor.execute(sql)
# mydb.commit()
#
#
# mycursor.execute("SELECT * FROM presensi")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)


# Menghapus Semua Data dari Tabel
# sql = "DELETE FROM presensi"
# mycursor.execute(sql)
# mydb.commit()

# mycursor.execute("SELECT * FROM presensi")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)