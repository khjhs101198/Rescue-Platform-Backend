#!/usr/bin/python
# -*- coding: UTF-8 -*-
import csv
import json
from RamdomLicence import RandomCar  


# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):
     
    # create a dictionary
    data = []
     
    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        i = 0
        # Convert each row into a dictionary 
        # and add it to data
        for rows in csvReader:
            # Assuming a column named 'No' to
            # be the primary key
            car = RandomCar()
            car1 = RandomCar()
            car2 = RandomCar()
            data.append({
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
                        "cars" : [
                            {   
                                "car_license_plate" : car["car_license_plate"],
                                "car_latitude" : float(rows['N']) ,
                                "car_longitude" : float(rows['E']),
                                "car_status" : car["car_status"] ,
                                "car_kind" : car["car_kind"]
                            },
                            {    
                                "car_license_plate" : car1["car_license_plate"],
                                "car_latitude" : float(rows['N']) ,
                                "car_longitude" : float(rows['E']),
                                "car_status" : car1["car_status"] ,
                                "car_kind" : car1["car_kind"]
                            },
                            {
                                "car_license_plate" : car1["car_license_plate"],
                                "car_latitude" : float(rows['N']) ,
                                "car_longitude" :float(rows['E']),
                                "car_status" : car1["car_status"] ,
                                "car_kind" : car1["car_kind"]
                            }
                        ]
                    }
                })
            i = i+1    
            #print(data)
            
    # Open a json writer, and use the json.dumps() 
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data,ensure_ascii=False))
         
# Driver Code
 
# Decide the two file paths according to your 
# computer system
csvFilePath = r'Names.csv'
jsonFilePath = r'Names.json'
# Call the make_json function
make_json("./output-merge.csv","./output-merge.json")


