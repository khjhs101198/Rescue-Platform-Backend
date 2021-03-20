import csv
import json
from .RamdomLicence import RandomCar 
# open output-merge.csv and merge fake car data to nested dictionary
def FirestationNestedDict():
	with open('/home/tsen65409/文件/Python/Flask/Edge-Seeds-List/SQL_data_preprocess/FireStation/output-merge.csv', encoding='utf-8') as csvf:
		csvReader = csv.DictReader(csvf)
		i = 0

		fire = {}
		for rows in csvReader:

			car = RandomCar()
			car1 = RandomCar()
			car2 = RandomCar()
			# dictionary
			data = {
				i : {
					"隊名" : rows['單位名稱'] ,
					"隸屬大隊" : rows['隸屬大隊'] ,
					"隸屬中隊" : rows['隸屬中隊'] ,
					"行政區域代碼" : rows['行政區域代碼'],
					"地址" : rows['地址'],
					"電話號碼" : rows['電話號碼'],
					"傳真號碼" : rows['傳真號碼'],
					"FireStation_latitude" : float(rows['N']),
					"FireStation_longitude" : float(rows['E']),	
					"cars" : {
						"car1" :{
							"car_license_plate" : car["car_license_plate"],
							"car_latitude" : float(rows['N']) ,
							"car_longitude" : float(rows['E']),
							"car_status" : car["car_status"] ,
							"car_kind" : car["car_kind"]
						},
						"car2" :{    
							"car_license_plate" : car1["car_license_plate"],
							"car_latitude" : float(rows['N']) ,
							"car_longitude" : float(rows['E']),
							"car_status" : car1["car_status"] ,
							"car_kind" : car1["car_kind"]
						},
						"car3" :{
							"car_license_plate" : car2["car_license_plate"],
							"car_latitude" : float(rows['N']) ,
							"car_longitude" :float(rows['E']),
							"car_status" : car1["car_status"] ,
							"car_kind" : car1["car_kind"]
						}
					}
				}	
			}
			i += 1
			# nested dictionary
			# ".update" will append a dictionary to main dictionary 
			fire.update(data)


	#print(fire[0]["隸屬中隊"])
	return (fire)
           