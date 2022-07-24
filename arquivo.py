from math import sqrt
arquivo = open("log.txt","+w")
lista = list(range(1,101))
k = 1
n = 0
while n < 100:
	
	for e in lista:
		arquivo.write(f"\n{k} -> Raiz = {str(sqrt(e))}")
		k += 1 
	n += 1
	k = 1
arquivo.close()
