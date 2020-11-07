import requests 
seeds = [
	{'seedID': 9527 ,'x' : 0.92,'y' : 232.32 ,'z' : -792.912 , 'n' : 24.8273133, 'e' : '' ,'battery' : 22 , 'status' : 1},
	
	{'seedID': 7789 ,'x' : 347.22 ,'y' : 4.3 ,'z' : 0.85 , 'n' : 23.8439271, 'e' : 120.97332641,'battery' : 87 , 'status' : 1},

	{'seedID': 0x222 ,'x' : 0.21297 ,'y' : 1.22 ,'z' : 4.82 ,'n' : 30.2975821 , 
	'e' : 189.5311421,'battery' : 33 , 'status' : 2}

	]
r = requests.post('http://0.0.0.0:2000/',json = seeds)
print(r.text)