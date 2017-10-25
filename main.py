import csv	
from biblioteca.funcao import *
'''
Projeto de algoritimo trabalhando com mineração de dados de acidentes
Desenvolvedor Gustavo Henrique Pereira
'''

scoreList=[]
MaiorSemana={"Domingo":0,"Sábado":0, "Segunda-feira" : 0 ,"Terça-feira" : 0 ,"Quarta-feira" : 0,"Quinta-feira" : 0 ,"Sexta-feira" : 0}
totalContagem=[]
dic={}
TipodeColisao={"Colisão com objeto móvel":0,"Danos Eventuais":0,"Atropelamento de pessoa": 0,"Colisão com bicicleta" : 0,"Não Informado" : 0,"Queda de motocicleta / bicicleta / veículo" : 0,"Colisão lateral" : 0 ,"Saída de Pista" : 0,"Colisão com objeto fixo" : 0,"Tombamento" :0,"Capotamento" :0,"Colisão Transversal" : 0,"Colisão frontal" : 0 , "Colisão traseira" : 0,"Incêndio" : 0 ,"Atropelamento de animal" : 0, "Derramamento de Carga" : 0 }
TiposDeFerimentos = {"Com vítimas fatais" : 0 ,"Com vítimas feridas" : {"Qtd. Feridos Graves" :0	,"Qtd. Feridos Leves" : 0},
	"Sem vítimas" :0}
RegiaodoBrasil={'NORTE' : {'AM':0,'RR' : 0,'PA' : 0 ,'TO': 0,'RO' : 0,'AC':0,'AP' : 0},
	'NORDESTE': {'MA':0,'PI':0,'BA':0,'RE':0,'AL':0,'SE':0,'PR':0,'RN':0,'PE':0,'CE':0,'PB':0},
	'CENTROOESTE':{'MT':0,'GO': 0,'MS':0,"DF":0},
	'SULDESTE' : {'MG':0,'ES':0,'RJ':0,'SP':0},
	'SUL' :{'PR':0,'SC':0,'RS':0}
	}
HorarioMax={"Manhã":{"01" :0 ,"02": 0,"03" : 0,"04" :0,"05" : 0,"06": 0,"07" : 0,"08": 0,"09": 0,"10" : 0,"11" : 0},
	"Tarde":{"13":0,"14":0,"15":0,"16":0,"17":0,"18":0},
	"Noite":{"19":0,"20":0,"21":0,"22":0,"23":0,"24":0,"00":0},
	"Meio dia":{"12":0}
	}
arquivo=input("Informe o arquivo : ")
tamanho=input("Informe o tamanho : ")
scoreList,num=ImportandoDados(scoreList,arquivo,tamanho)
TipodeColisao=TipodeColisaoFx(TipodeColisao,scoreList)
RegiaodoBrasil=IndiceDosEstados(RegiaodoBrasil,scoreList)
ExporntandoREGIAO(RegiaodoBrasil)

