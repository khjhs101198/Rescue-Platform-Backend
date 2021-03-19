import random
import string
import json
# This program is to create fake vehicle data for firestation.
def RandomCar():
	prefix = "".join(random.sample(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'], 3))

	prefix = prefix + "-"

	suffix = "".join(random.sample(['1','2','3','4','5','6','7','8','9','0'], 4))
	car_license_plate = prefix + suffix 

	car_longitude = "120." + "".join(random.sample(['1','2','3','4','5','6','7','8','9','0'], 7))
	car_latitude = "22." + "".join(random.sample(['1','2','3','4','5','6','7','8','9','0'], 7))
	car_status = 0
	car_kind = "".join(random.sample(['0','1'], 1))

	car_info = {"car_license_plate": car_license_plate,
			"car_latitude" : float(car_latitude) ,
			"car_longitude" : float(car_longitude),
			"car_status" : car_status ,
			"car_kind" : int(car_kind)
		}
	#print(car_info)
	return(car_info)
RandomCar()