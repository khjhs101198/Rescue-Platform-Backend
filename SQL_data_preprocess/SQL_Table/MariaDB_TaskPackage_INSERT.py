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

    sql = "INSERT INTO task_package(id , latitude, longitude, task_date, taskinfo)VALUES (%s,%s,%s,%s,%s);"

    new_data = (1, 23.161645572986895, 120.64251171091588)
    cursor.execute(sql, new_data)

    new_data = (2, 23.161645572986895, 120.64251171091588)
    cursor.execute(sql, new_data)
    
    new_data = (3, 23.161645572986895, 120.64251171091588)
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