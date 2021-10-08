# -*- coding: utf-8 -*-
"""
Created on Mon May  3 22:50:32 2021

@author: LENOVO
"""
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="q12we3",
)  

editDb = mydb.cursor()

# editDb.execute("create database Tugas_2_NizanDhiaulhaq")
editDb.execute("use Tugas_2_NizanDhiaulhaq")
# editDb.execute("create table wishlist(id int(5),namaProduk char(50), jumlah int, total_harga int, link_produk varchar(200))")

# editDb.execute("desc wishlist")


    
# query = "INSERT INTO wishlist VALUES (%s, %s, %s,%s,%s)"
# val = [(1,"Mainan Lego",10,100000,"https//www.Tokpedulu.com/adcjaskd"),
#         (2,"Keyboard Mechanical Wireless",1,1000000,"https//www.Tokpedulu.com/asdasadcjaskd"),
#         (3,"Peci Gajah Duduk",5,500000,"https//www.Tokpedulu.com/adcjaskdgdurygd"),
#         (4,"Tutup Botol Murah",30,3000,"https//www.Tokpedulu.com/adcjaskdfhjyujhg"),
#         (5,"Botol Plastik Bekas",50,10000,"https//www.Tokpedulu.com/adcjaskdfdytrydgg")]

# for i in val:
#     editDb.execute(query,i)
#     mydb.commit()

# editDb.execute("show tables")    

# for x in editDb:
#     print(x)

# editDb.execute("select * from wishlist")

# for x in editDb:
#     print(x)
    
# print("======update======")    
# query = "update wishlist set namaProduk='Bukan Peci' where id=3"
# editDb.execute(query)
# mydb.commit()

# editDb.execute("select * from wishlist")

# for x in editDb:
#     print(x)
    
print("======delete======")
query = "delete from wishlist where id=1"
editDb.execute(query)
mydb.commit()


editDb.execute("select * from wishlist")
for x in editDb:
    print(x)
