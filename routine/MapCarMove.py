#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests 
import time
def Jiaxian2seeds1():
    path = '路徑_甲仙_2_seed1.txt'
    f = open(path, 'r')
    cars = []
    for line in f.readlines():
        #以 "," 來切割字串
        str1 = line.split(',')
        #print(str1)
        print(len(str1))
        for i in range(0,len(str1),2):
            # 擷取特定字串
            str_latitude = str(str1[i])
            str_longitude = str(str1[i+1])
            # 去除 "("   ")"
            str_latitude = str_latitude.replace('(','')
            str_longitude = str_longitude.replace(')','')
            # append dictionary to Carpath

            cars = [{
                'car_license_plate' :"FKX-6230" , 
                'car_latitude' : float(str_latitude),
                'car_longitude' : float(str_longitude)
                }]
            r = requests.post('http://0.0.0.0:3000/ChangeCarItude',json = cars)
            print(r.text)
            print("sleep 0.01 seconds.")
            time.sleep(0.001)
    cars = [{
        'car_license_plate' :"FKX-6230" , 
        'car_latitude' : 23.0833145,
        'car_longitude' : 120.5902528
        }]
    r = requests.post('http://0.0.0.0:3000/ChangeCarItude',json = cars)
    print("back to Jiaxian")

    f.close

Jiaxian2seeds1()