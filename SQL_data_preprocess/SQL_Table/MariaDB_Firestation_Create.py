import mysql.connector
from mysql.connector import Error
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
    sql ='''CREATE TABLE Firestation(
        team_name CHAR(50) NOT NULL,
        brigade CHAR(50) NOT NULL,
        squadron CHAR(50) NOT NULL,
        area_code INT,
        address VARCHAR(500),
        phone_number CHAR(50),
        dax_number  CHAR(50),
        fireStation_latitude DECIMAL(10,7) NOT NULL,
        fireStation_longitude DECIMAL(10,7) NOT NULL,
        PRIMARY KEY(Team_name)
    );'''
    cursor.execute(sql)

    #Closing the connection
    connection.close()

except Error as e:
    print("資料庫連接失敗：", e)

finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("資料庫連線已關閉")