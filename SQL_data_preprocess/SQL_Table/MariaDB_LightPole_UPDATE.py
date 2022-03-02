#!/usr/bin/python
#-*- coding: utf-8 -*-
import mysql.connector
from mysql.connector import Error
from Datetime_To import * 
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
    cursor = connection.cursor()
    #Creating table as per requirement
    sql = "UPDATE light_pole SET token =%s WHERE id = %s;"

    date_str = GetStrDate()
    date_int = StrDateToInt(date_str)

    letter = date_int % 26
    token_A = chr(letter+65)

    for i in range(1,6):
        token_B = date_int * i
        token_B = StrDateToInt(str(token_B))

        tokenstr = token_A + "-" + str(token_B) 

        new_data = (tokenstr,i)
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