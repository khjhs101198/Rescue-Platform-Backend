#!/usr/bin/python
#-*- coding: utf-8 -*-
import mysql.connector
from mysql.connector import Error
import datetime
from datetime2int import datetimeTOint 
try:
    # 連接 MySQL/MariaDB 資料庫
    connection = mysql.connector.connect(
        host='localhost',          # 主機名稱
        database='smartdb', # 資料庫名稱
        user='Tsen',        # 帳號
        password='CTsen')  # 密碼

    if connection.is_connected():

        # 顯示資料庫版本
        db_Info = connection.get_server_info()
        print("資料庫版本：", db_Info)

        # 顯示目前使用的資料庫
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print("目前使用的資料庫：", record)
    Fire = FirestationNestedDict()   
    cursor = connection.cursor()
    i = 0    
    #Creating table as per requirement
    sql = "INSERT INTO light_pole(id, token, time_phase) VALUES (%s,%s,%s);"
    dateint = datetimeTOint()
    letter = dateint % 26
    token = chr(letter+65)
    tokenstr = token + "-" + str(dateint) 
    print(tokenstr)
    for i in 5:
        new_data = (i,tokenstr,1)
        cursor.execute(sql, new_data)
    connection.commit()
    #Closing the connection
    connection.close()

except Error as e:
    print("資料庫連接失敗：", e)

finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("資料庫連線已關閉")