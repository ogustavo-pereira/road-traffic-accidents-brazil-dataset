'''
Projeto de algoritimo trabalhando com mineração de dados de acidentes
Desenvolvedor Gustavo Henrique Pereira
'''
from datetime import date
import csv
##Coletando dado
def ImportandoDados(scoreList,arquivo,tamanho) :
	num=0
	with open(arquivo, "rt", encoding="UTF-8") as csvfile:
			scoreFileReader = csv.reader(csvfile)
			for row in scoreFileReader:
				if len(row) != 0 :
					num=num+1
					scoreList = scoreList + [row]
					print(num/int(tamanho)*100)
	
	csvfile.close()
	return scoreList,num

##Função retorna o dia da semana que há mais acidente
def IndiceDaSemana(MaiorSemana,scoreList) :
	dias = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')
	DadosSemana=[]
	dt=	[]
	for elm in scoreList :
		DadosSemana=DadosSemana+[elm[3]]
	for hj in DadosSemana :
		dividido=hj.split(" ")
		dt=dividido[0].split("/")
		dt[0]=int(dt[0])+0
		dt[1]=int(dt[1])+0
		dt[2]=int(dt[2])+0
		num=date(dt[2],dt[1],dt[0]).weekday()
		MaiorSemana[dias[num]]=MaiorSemana[dias[num]]+1
	return MaiorSemana


##função retorna o Horario com mais indicies
def InciceDaHora(HorarioMax,scoreList):
	for elm in scoreList :
		item=elm[3]
		data,hora=item.split(" ")
		horadiv,minutosdiv,segundosdiv=hora.split(":")
		if(horadiv in HorarioMax["Manhã"]) :
			if(HorarioMax['Manhã'][horadiv]==0):
				HorarioMax['Manhã'][horadiv]={}
				y={hora:1}
				HorarioMax['Manhã'][horadiv].update(y)
			if(hora in HorarioMax['Manhã'][horadiv]) :
				HorarioMax['Manhã'][horadiv][hora]=HorarioMax['Manhã'][horadiv][hora]+1
			else:
				y={hora:1}
				HorarioMax['Manhã'][horadiv].update(y)

		elif(horadiv in HorarioMax["Tarde"]) :
			if(HorarioMax['Tarde'][horadiv]==0):
				HorarioMax['Tarde'][horadiv]={}
				y={hora:1}
				HorarioMax['Tarde'][horadiv].update(y)
			if(hora in HorarioMax['Tarde'][horadiv]) :
				HorarioMax['Tarde'][horadiv][hora]=HorarioMax['Tarde'][horadiv][hora]+1
			else:
				y={hora:1}
				HorarioMax['Tarde'][horadiv].update(y)
		elif(horadiv in HorarioMax["Noite"]) :
			if(HorarioMax['Noite'][horadiv]==0):
				HorarioMax['Noite'][horadiv]={}
				y={hora:1}
				HorarioMax['Noite'][horadiv].update(y)
			if(hora in HorarioMax['Noite'][horadiv]) :
				HorarioMax['Noite'][horadiv][hora]=HorarioMax['Noite'][horadiv][hora]+1
			else:
				y={hora:1}
				HorarioMax['Noite'][horadiv].update(y)
		elif(horadiv in HorarioMax["Meio dia"]) :
			if(HorarioMax['Meio dia'][horadiv]==0):
				HorarioMax['Meio dia'][horadiv]={}
				y={hora:1}
				HorarioMax['Meio dia'][horadiv].update(y)
			if(hora in HorarioMax['Meio dia'][horadiv]) :
				HorarioMax['Meio dia'][horadiv][hora]=HorarioMax['Meio dia'][horadiv][hora]+1
			else:
				y={hora:1}
				HorarioMax['Meio dia'][horadiv].update(y)
			

		else:
			print(horadiv)
			print("nao entrou FX Horas")
	return HorarioMax

##Indica o Indice de ferimentos
def IndiceSituacao(TiposDeFerimentos,scoreList) :
	for elm in scoreList :
		TiposDeFerimentos["Com vítimas fatais"] = TiposDeFerimentos["Com vítimas fatais"]+int(elm[15])
		TiposDeFerimentos["Com vítimas feridas"]["Qtd. Feridos Graves"] = TiposDeFerimentos["Com vítimas feridas"]["Qtd. Feridos Graves"]+int(elm[16])
		TiposDeFerimentos["Com vítimas feridas"]["Qtd. Feridos Leves"] = TiposDeFerimentos["Com vítimas feridas"]["Qtd. Feridos Leves"]+int(elm[17])
		TiposDeFerimentos["Sem vítimas"] = TiposDeFerimentos["Sem vítimas"]+int(elm[18])
	return TiposDeFerimentos


##Indica Indice de do Tipos de Colisão
def TipodeColisaoFx(TipodeColisao,scoreList) :
	for elm in scoreList :
	 	item=elm[13]
	 	TipodeColisao[item]=TipodeColisao[item]+1
	return TipodeColisao

##Indica o indice por estados
def IndiceDosEstados(RegiaodoBrasil,scoreList) :
	for uf in scoreList :
		if(uf[5] in RegiaodoBrasil['NORTE']) :
			if(RegiaodoBrasil['NORTE'][uf[5]]==0) :
				RegiaodoBrasil['NORTE'][uf[5]]={}
				y={uf[9]:1}
				RegiaodoBrasil['NORTE'][uf[5]].update(y)
			if (uf[9] in RegiaodoBrasil['NORTE'][uf[5]]):
				RegiaodoBrasil['NORTE'][uf[5]][uf[9]]=RegiaodoBrasil['NORTE'][uf[5]][uf[9]]+1
			else:
				y={uf[9]:1}
				RegiaodoBrasil['NORTE'][uf[5]].update(y)
		elif(uf[5] in RegiaodoBrasil['NORDESTE']) :
			if(RegiaodoBrasil['NORDESTE'][uf[5]]==0) :
				RegiaodoBrasil['NORDESTE'][uf[5]]={}
				y={uf[9]:1}
				RegiaodoBrasil['NORDESTE'][uf[5]].update(y)
			if (uf[9] in RegiaodoBrasil['NORDESTE'][uf[5]]):
				RegiaodoBrasil['NORDESTE'][uf[5]][uf[9]]=RegiaodoBrasil['NORDESTE'][uf[5]][uf[9]]+1
			else:
				y={uf[9]:1}
				RegiaodoBrasil['NORDESTE'][uf[5]].update(y)

		elif(uf[5] in RegiaodoBrasil['SULDESTE']) :
			if(RegiaodoBrasil['SULDESTE'][uf[5]]==0) :
					RegiaodoBrasil['SULDESTE'][uf[5]]={}
					y={uf[9]:1}
					RegiaodoBrasil['SULDESTE'][uf[5]].update(y)
			if (uf[9] in RegiaodoBrasil['SULDESTE'][uf[5]]):
				RegiaodoBrasil['SULDESTE'][uf[5]][uf[9]]=RegiaodoBrasil['SULDESTE'][uf[5]][uf[9]]+1
			else:
				y={uf[9]:1}
				RegiaodoBrasil['SULDESTE'][uf[5]].update(y)

		elif(uf[5] in RegiaodoBrasil['SUL']) :
			if(RegiaodoBrasil['SUL'][uf[5]]==0) :
				RegiaodoBrasil['SUL'][uf[5]]={}
				y={uf[9]:1}
				RegiaodoBrasil['SUL'][uf[5]].update(y)
			if (uf[9] in RegiaodoBrasil['SUL'][uf[5]]):
				RegiaodoBrasil['SUL'][uf[5]][uf[9]]=RegiaodoBrasil['SUL'][uf[5]][uf[9]]+1
			else:
				y={uf[9]:1}
				RegiaodoBrasil['SUL'][uf[5]].update(y)
		elif(uf[5] in RegiaodoBrasil['CENTROOESTE']) :
			if(RegiaodoBrasil['CENTROOESTE'][uf[5]]==0) :
				RegiaodoBrasil['CENTROOESTE'][uf[5]]={}
				y={uf[9]:1}
				RegiaodoBrasil['CENTROOESTE'][uf[5]].update(y)
			if (uf[9] in RegiaodoBrasil['CENTROOESTE'][uf[5]]):
				RegiaodoBrasil['CENTROOESTE'][uf[5]][uf[9]]=RegiaodoBrasil['CENTROOESTE'][uf[5]][uf[9]]+1
			else:
				y={uf[9]:1}
				RegiaodoBrasil['CENTROOESTE'][uf[5]].update(y)
		else:
			print(uf[5])
			print("nao entrou REGIÃO")
	return RegiaodoBrasil

##EXPORTA PARA UM ARQUIVO CSV O HORARIO
def ExportarHoras(HorarioMax):
	with open('Horas.csv', 'w') as csvfile:
		fieldnames = ['Manhã','Meio dia','Tarde','Noite']
		resultado={'Manhã' :0,'Meio dia': 0,'Tarde':0,'Noite':0}
		for vetor in HorarioMax:
			for elm in HorarioMax[vetor] :
				if(HorarioMax[vetor][elm]!=0):
					resultado[vetor]= resultado[vetor] +sum(HorarioMax[vetor][elm].values())
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		writer.writerow(resultado)
		spamwriter = csv.writer(csvfile, delimiter=' ',
		quotechar=' ', quoting=csv.QUOTE_MINIMAL)
		spamwriter.writerow("")
		spamwriter.writerow("Por Horas :")
		horas=HorarioMax["Manhã"]
		horas.update(HorarioMax["Tarde"])
		horas.update(HorarioMax["Noite"])
		horas.update(HorarioMax["Meio dia"])
		writer2 = csv.DictWriter(csvfile, fieldnames=horas)
		writer2.writeheader()
		num=0
		for vetor in horas :
			if(horas[vetor]!=0):
				num=num+sum(horas[vetor].values())
			horas[vetor]=num
			num=0
		writer2.writerow(horas)
		print("DADOS EXPORTADOS")

##EXPORTA PARA UM ARQUIVO CSV O SEMANA
def ExportandoDias(MaiorSemana):
	with open('maiorsemana.csv', 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=MaiorSemana)
		writer.writeheader()
		writer.writerow(MaiorSemana)

##EXPORTA PARA UM ARQUIVO CSV O HORARIO
def ExportandoDias(MaiorSemana):
	with open('maiorsemana.csv', 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=MaiorSemana)
		writer.writeheader()
		writer.writerow(MaiorSemana)

##EXPORTA PARA UM ARQUIVO CSV O TIPOS DE FERIMENTOS
def ExpotandoTiposDeFerimentos(TiposDeFerimentos):
	with open('tiposdeferimentos.csv', 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=TiposDeFerimentos)
		writer.writeheader()
		writer.writerow(TiposDeFerimentos)

##EXPORTA PARA UM ARQUIVO CSV O TIPOS DE COLISÂO
def ExpotandoTiposDeFerimentos(TipodeColisao):
	with open('tiposdeferimentos.csv', 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=TipodeColisao)
		writer.writeheader()
		writer.writerow(TipodeColisao)


def ExporntandoREGIAO(RegiaodoBrasil):
	Regiao={"NORTE": 0,"NORDESTE" : 0, "SUL" : 0 , "SULDESTE" : 0 ,"CENTROOESTE" : 0}
	for elm in Regiao:
		for elm2 in RegiaodoBrasil[elm] :
			if(RegiaodoBrasil[elm][elm2]!=0):
				Regiao[elm]=Regiao[elm] +sum(RegiaodoBrasil[elm][elm2].values())
	print(Regiao)
	estados={}
	for elm in RegiaodoBrasil:
		for elm2 in RegiaodoBrasil[elm]:
			if(elm2 in estados ):
				if(RegiaodoBrasil[elm][elm2]!= 0):
					regist=sum(RegiaodoBrasil[elm][elm2].values())
					estado[elm2]=estado[elm2]+regist
			else:
				if(RegiaodoBrasil[elm][elm2]!= 0):
					regist=sum(RegiaodoBrasil[elm][elm2].values())
					y={elm2 : regist}
					estados.update(y)

	print (estados)


			

	with open('Regiao.csv', 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=Regiao)
		writer.writeheader()
		writer.writerow(Regiao)

		spamwriter = csv.writer(csvfile, delimiter=' ',
		quotechar=' ', quoting=csv.QUOTE_MINIMAL)
		spamwriter.writerow("")
		for elm in estados:
			spamwriter.writerow([(elm),",",(estados[elm])])
		spamwriter.writerow("")
		for elm in RegiaodoBrasil:
			for elm2 in RegiaodoBrasil[elm]:
				if(RegiaodoBrasil[elm][elm2]!=0) :
					for final in RegiaodoBrasil[elm][elm2] :
						spamwriter.writerow([final,",",RegiaodoBrasil[elm][elm2][final]])



				
