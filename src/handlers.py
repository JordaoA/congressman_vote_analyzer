# coding: utf-8
import numpy as np
import pandas as pd

#Traduz um determinado DataFrame para um dicionario
def dataFrameToDic(dataFrame,dic):
	for i in range(len(dataFrame)):
		partido = dataFrame.partido[i]
		voto = dataFrame.voto[i]
		
		if partido not in dic:
			dic[partido] = (partido,{voto:[voto,1]})
		
		else:
			if voto not in dic[partido][1]:
				dic[partido][1][voto] = [voto,1]
			else:
				dic[partido][1][voto][1] += 1

#Separa a lista para criação de Data Frame especial a partir de dicionario
def separaEmLista(dictionary):
	toReturn = []
	for i in dictionary:
		auxDic = {-1: 0, 0: 0, 1: 0, 2: 0, 3: 0}
		
		for j in dictionary[i][1]:
			if j in auxDic:
				auxDic[j] = dictionary[i][1][j][1]
		
		toReturn.append([i,auxDic[-1],auxDic[0],auxDic[1],auxDic[2],auxDic[3]])

	return toReturn

def filtraDados(ano):
	partidos = {}
	labels = ["partido","Votos-1","Votos0","Votos1","Votos2","Votos3"]
	data = pd.read_csv("../data/pure_Data/votacoes_"+ ano +".csv",",")
	dataFrameToDic(data, partidos)
	listaVotos = separaEmLista(partidos)
	return pd.DataFrame(listaVotos,columns = labels)

def preparaMenu(dataFrame):
	titles = []
	lenOfDataFrame = len(dataFrame) 
	for i in range(lenOfDataFrame):
		titles.append((dataFrame.partido[i],i))
	return titles

def median(lista):
    n = len(lista)
    s = sorted(lista)
    return (sum(s[n//2-1:n//2+1])/2.0, s[n//2])[n % 2] if n else None