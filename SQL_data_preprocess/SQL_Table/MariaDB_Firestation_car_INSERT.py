#!/usr/bin/python
#-*- coding: utf-8 -*-
import mysql.connector
from mysql.connector import Error
from FireStation.FireStationCSV_2_Dict import FirestationNestedDict 
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
    sql = "INSERT INTO firestation_car(car_license_plate, team_name,car_latitude ,car_longitude,car_status,car_kind) VALUES (%s, %s, %s,%s, %s, %s);"
    for i in Fire:
        new_data = (Fire[i]["cars"]["car1"]["car_license_plate"], 
                    Fire[i]["隊名"], 
                    Fire[i]["cars"]["car1"]["car_latitude"],
                    Fire[i]["cars"]["car1"]["car_longitude"],
					Fire[i]["cars"]["car1"]["car_status"],
					Fire[i]["cars"]["car1"]["car_kind"])
        cursor.execute(sql, new_data)
        new_data = (Fire[i]["cars"]["car2"]["car_license_plate"], 
                    Fire[i]["隊名"], 
                    Fire[i]["cars"]["car2"]["car_latitude"],
                    Fire[i]["cars"]["car2"]["car_longitude"],
				    Fire[i]["cars"]["car2"]["car_status"],
				    Fire[i]["cars"]["car2"]["car_kind"])
        cursor.execute(sql, new_data)
        new_data = (Fire[i]["cars"]["car3"]["car_license_plate"], 
                    Fire[i]["隊名"], 
                    Fire[i]["cars"]["car3"]["car_latitude"],
                    Fire[i]["cars"]["car3"]["car_longitude"],
                    Fire[i]["cars"]["car3"]["car_status"],
                    Fire[i]["cars"]["car3"]["car_kind"])
        cursor.execute(sql, new_data)
        i+= 1
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