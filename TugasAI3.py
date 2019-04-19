import csv

def down(atas,bawah,x) :
	return (atas-x)/(atas-bawah)
	
def up(atas,bawah,x) :
	return (x-bawah)/(atas-bawah)
	
def rendah(x) :
	if (x <= 53) :
		return 1
	elif (x > 53) and (x < 55) :
		return down(55,53,x)
	else:
		return 0
		
def menengah(x) :
	if (x >= 55) and (x <= 65 ) :
		return 1
	elif(x > 53) and (x < 55) :
		return up(55,53,x)
	elif(x>65) and (x<70) :
		return down(70,65,x)
	else :
		return 0

def tinggi(x) :
	if (x>=70) and (x<=75):
		return 1
	elif(x>65) and (x<70):
		return up(70,65,x)
	elif(x>75) and (x<80):
		return down(80,75,x)
	else :
		return 0

def sangat_tinggi(x):
	if(x>=80): 
		return 1
	elif(x>75) and (x<80):
		return up(80,75,x)
	else:
		return 0

def kurang(y):
	if(y<=40):
		return 1
	elif(y>40) and (y<45):
		return down(45,40,y)
	else:
		return 0

def cukup(y):
	if(y>=45) and (y<=55):
		return 1
	elif(y>40) and (y<45):
		return up(45,45,y)
	elif(y>57) and (y<64):
		return down(64,57,y)
	else:
		return 0

def baik(y):
	if(y>=64) and (y<=71):
		return 1
	elif(y>57) and (y<64):
		return up(64,57,y)
	elif(y>71) and (y<75):
		return down(75,71,y)
	else:
		return 0

def sangat_baik(y):
	if(y>=75):
		return 1
	elif(y>71) and (y<75):
		return up(75,71,y)
	else:
		return 0

def diterima(x,y):
	D1 = min(rendah(x), sangat_baik(y))
	D2 = min(menengah(x), sangat_baik(y))
	D3 = min(menengah(x), baik(y))
	D4 = min(tinggi(x), sangat_baik(y))
	D5 = min(tinggi(x), baik(y))
	D6 = min(tinggi(x), cukup(y))
	D7 = min(sangat_tinggi(x), sangat_baik(y))
	D8 = min(sangat_tinggi(x), baik(y))
	D9 = min(sangat_tinggi(x), cukup(y))
	return max(D1,D2,D3,D4,D5,D6,D7,D8,D9)

def ditolak(x,y):
	T1 = min(sangat_tinggi(x), kurang(y))
	T2 = min(tinggi(x), kurang(y))
	T3 = min(menengah(x), cukup(y))
	T4 = min(menengah(x), kurang(y))
	T5 = min(rendah(x), baik(y))
	T6 = min(rendah(x), cukup(y))
	T7 = min(rendah(x), kurang(y))
	return max(T1,T2,T3,T4,T5,T6,T7)

header = []
answer = [] 
i = 0

def tentukan() :
	x = float(row[1])
	y = float(row[2])
	Dmax = diterima(x,y)
	DTmax = ditolak(x,y)
	if(Dmax >= DTmax):
		data = [row[0], x, y, 'Ya']
		answer.append(data)
	else :
		data = [row[0], x, y, 'Tidak']
		answer.append(data)


with open('DataTugas3.csv') as rfile:
	reader = csv.reader(rfile)
	for row in reader:
		if i == 0:
			data = [row[0], row[1], row[2], 'diterima']
			header.append(data)
			i = 1
		else :
			tentukan()


wfile = open('TebakanTugas3.csv', 'w', newline="")
writer = csv.writer(wfile)
writer.writerows(header)
writer.writerows(answer)
wfile.close()