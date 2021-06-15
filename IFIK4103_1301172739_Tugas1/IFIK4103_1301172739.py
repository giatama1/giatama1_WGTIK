import numpy as np
#batasX = [-3,3]
#batasY = [-2,2]

SumGenerasi = 10
SumPopulasi = 350
SumDNA = 10
crossRate = 0.65
MutasiRate = 0.015

def BinerToDesimalX(populasi):
	MaxSum = 0
	panjangDNAx = (SumDNA/2)+1
	hasilPanjangDNAx = int(panjangDNAx)
	
	x = np.zeros([SumPopulasi],dtype = float)

	for i in range(1, hasilPanjangDNAx):
		MaxSum = MaxSum + 2**(-i)
	for i in range (SumPopulasi):
		for j in range (1, hasilPanjangDNAx):
			x[i] = x[i] + populasi[i][j-1]*(2**-j)
		x[i] = (-3+((3-(-3))/MaxSum)*x[i])

	return x


def BinerToDesimalY(populasi):
	MaxSum = 0
	panjangDNAy = SumDNA/2
	hasilPanjangDNAy = int(panjangDNAy)
	
	y = np.zeros([SumPopulasi],dtype = float)

	for i in range(hasilPanjangDNAy, SumDNA):
		MaxSum = MaxSum + 2**(-i)
	for i in range (SumPopulasi):
		for j in range (hasilPanjangDNAy, SumDNA):
			y[i] = y[i] + populasi[i][j]*(2**-j)
		y[i] = (-2+((2-(-2))/MaxSum)*y[i])
	return y
 
def nilaiDecode(x,y):
	nilai = (4-2.1*(x**2)+((x**4)/3))*(x**2)+x*y+((-4)+(4*(y**2)))*(y**2)
	return nilai

def fitness(nilai):
	fitness = abs(1/nilai)
	return fitness

def RouletteWheel(populasi):
	panjangFitness = fitness(nilaiDecode(BinerToDesimalX(populasi),BinerToDesimalY(populasi)))
	jumlahFitness = panjangFitness.sum()
	kumulatifFitnes = 0
	nilaiRandom = np.random.uniform(0,1)
	i = 0
	while i <= len(populasi):
		kumulatifFitnes = kumulatifFitnes + panjangFitness[i]
		if ( (kumulatifFitnes/jumlahFitness)>nilaiRandom) :
			index = i
			break 
		i = i+1
	return index    

def CrossOver(parent1,parent2,jumlahDNA,populasi):
	Parent1 = populasi[parent1]
	Parent2 = populasi[parent2]
	nilaiRand = np.random.uniform(0,1)
	if (nilaiRand < crossRate):
		titikPotong = 1+ int(np.ceil(np.random.randint(SumDNA-1)))
		child1 = np.concatenate([Parent1[0:titikPotong],Parent2[titikPotong+0:jumlahDNA]])
		child2 = np.concatenate([Parent2[0:titikPotong],Parent1[titikPotong+0:jumlahDNA]])
		populasi[parent1] = child1
		populasi[parent2] = child2
	return populasi

		
def Mutasi(kromosom,jumlahDNA,MutasiRate):
	nilaiRand = np.random.uniform(0,1)
	mutasiKrom = kromosom
	for i in range (1,SumDNA):
		if (nilaiRand < MutasiRate):
			if (kromosom[i] == 0):
				mutasiKrom[i] = 1
			else:
				mutasiKrom[i] = 0

def Minimum(nilai):
	for index in nilai:
		minimum = 99
		if index < minimum:
			minimum = index
	return minimum

#def SteadyState():
isiIndex = np.zeros([SumPopulasi],dtype = float)
populasi = np.random.randint(2, size = (SumPopulasi,SumDNA))
i = 1
while i <= SumGenerasi:
	Fitness = fitness(nilaiDecode(BinerToDesimalX(populasi),BinerToDesimalY(populasi)))
	populasi = CrossOver(RouletteWheel(populasi),RouletteWheel(populasi),SumDNA,populasi)
	for pop in populasi :
		pop = Mutasi(pop,SumDNA,MutasiRate)
	
	nilaiX1 = BinerToDesimalX(populasi)
	nilaiX2 = BinerToDesimalY(populasi)
	nilaiFungsi = nilaiDecode(BinerToDesimalX(populasi),BinerToDesimalY(populasi))
	nilaiMinimumFungsi = Minimum(nilaiFungsi)
	nilaiFitness = fitness(nilaiDecode(BinerToDesimalX(populasi),BinerToDesimalY(populasi)))
	print("----------------------------Generasi",i,"----------------------------------")
	populasiMinimum = populasi[np.argmax(nilaiMinimumFungsi),:] 
	print(populasiMinimum)
	#print("Nilai X1             : ",Dua_BinerToDesimalX(populasiMinimum))
	#print("Nilai X2 			: ",BinerToDesimalY(populasiMinimum))
	#print("Nilai Fitness        : ",fitness(nilaiDecode(BinerToDesimalX(populasiMinimum),BinerToDesimalY(populasiMinimum))))
	print("Nilai Minimum Fungsi : ",nilaiMinimumFungsi)
	i=i+1
