#Programa que converte .pdf em .txt
#Sintaxe: python3 pdf_to_txt.py nome_do_arquivo.pdf 
#arquivo de saída: nome_do_arquivo.pdf.txt -> Ele só concatena a string do nome do arquivo de entrada com a extensão ".txt"
#Deve-se atentar à codificação de caracteres do .pdf Ex: UTF-8, dependendo da codificação, o programa dá erro.
import PyPDF2
import sys
import os
import nltk
lista = [] #Lista_vazia!!!
nome_arquivo = sys.argv #Digitar o nome do arquivo!!!
arquivos = [] #lista vazia dos arquivos na pasta.
for a in os.listdir("."):
	arquivos.append(a)  #Cria lista com nome de arquivos na pasta!!!

try:
	if (nome_arquivo[1] in (arquivos)):
		pdffileobj=open((nome_arquivo[1]),'rb')  #Compara o nome do arquivo .pdf (parâmetro) com o arquivo presente na pasta atual.
#create reader variable that will read the pdffileobj
	print(str(nome_arquivo[1]))
	pdfreader=PyPDF2.PdfFileReader(pdffileobj, strict = False)
 
	for k in range(0,pdfreader.numPages): 
		pageobj=pdfreader.getPage(k) 

		text=pageobj.extractText()
		lista.append(text)

	nome_saida = nome_arquivo[1] + ".txt"
	with open((nome_saida),"w") as file1: #Limpa os dados do arquivo anterior a cada vez que o programa é executado.
		for k in range (0,len(lista)):
			file1.write(lista[k])
	
	LARGURA = int(input("Quantidade de caracteres por linha? ")) #Quantidade de caracteres por linha é setada pelo usuário.
	nome_saida2 = nome_arquivo[1] + "2" + ".txt"
	lista = []
	N_caracteres = 0
	k = 0
	string = []
	with open((nome_saida),"rb") as file1, open((nome_saida2),"w") as file2: #Trecho do código para estimar número de caracteres do arquivo gerado em .txt
			while k < os.path.getsize(nome_saida):    #os.path.getsize() -> tamanho do arquivo de saída.
				string = file1.read(LARGURA)       
				file2.write(f"{string[0:LARGURA-1]}\n")
				k = k+LARGURA
	
	k = 0
	with open ((nome_saida),"rb") as file1, open("tokens.txt","a") as tokens:
		while k < os.path.getsize(nome_saida):    #os.path.getsize() -> tamanho do arquivo de saída.
			string = file1.read(LARGURA)       
			token = nltk.word_tokenize(str(string))
			tokens.write(f"\n{str(token)}")          #Salva todos os tokens dos arquivos em .txt!
			k = k+LARGURA 
			
	
	#print(f"Tokenização: {token}")   #--------Tokenização tá meio capenga!!!--------------- 
					  #----Melhorar essa parte-----------------------------
	
	print(f"\n\n Arquivo salvo com o nome: {nome_saida2}")	

except FileNotFoundError:                    
	print("\nArquivo não encontrado!!!")
	print("\nExiste esse arquivo na pasta???")
except NameError:
	print("\nNome não encontrado!!!")
	print("\nExiste esse arquivo na pasta???")
except UnicodeEncodeError:
	print("\nFormatação do texto incompatível, deve-se alterá-la!!!")

