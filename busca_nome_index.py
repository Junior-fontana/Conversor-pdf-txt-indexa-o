import sys
import nltk

#string = str(input("Palavra a ser digitada: "))
token = input("\nDigite as palvras-chave: ")
string = nltk.word_tokenize(str(token))
#string = sys.argv #lista que corresponde à string (parâmetro) ao momento da execução do código.
flag = 0
k = 1

def busca_palavra(parametro, arquivo):
	conta = 0
	for palavra in arquivo.readlines():
		if parametro in palavra:
			conta += 1
			print(f"Palavra '{parametro}' encontrada {conta} vezes!!!")
			
while k < len(string):
	with open("tokens.txt","r") as arquivo:
		#for palavra in arquivo.readlines():
		#if string[k] in palavra: ##A string começa a partir do segundo parâmetro, o primeiro é o comando da         
		busca_palavra(string[k],arquivo)
				    ###execução do programa.
				##print("Palavra encontrada!!!")
			#	flag = 1
			#	conta += 1
			#	if flag == 1:
			#		print(f"\nA palavra '{string[k]}' foi encontrada {conta} vezes!!!")
			#		flag = 0
			#else:
		#		print(f"Palavra '{string[k]}' Não encontrada!!!")
	k += 1
print(len(string))

