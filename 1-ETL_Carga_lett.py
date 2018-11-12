#Conexao com base de dados
import pymysql

from requests import get
from bs4 import BeautifulSoup

#Argumentos para estabelecer conexao com o banco de dados MySql SELECT
cnxn = pymysql.connect(host='localhost', db='letter', user='root', passwd='123456')
#Atribuicao para conexao
cursor = cnxn.cursor()
#Query para coleta de Dados

#Argumentos para estabelecer conexao com o banco de dados MySql INSERT
cnxii = pymysql.connect(host='localhost', db='lett', user='root', passwd='123456')
#Atribuicao para conexao
cursorLett = cnxii.cursor()

loja = [58, 73, 62, 63, 61, 59, 134, 165, 159, 162, 60, 128, 174, 120, 113, 133, 101, 116, 125, 141, 132, 182, 131, 109, 94, 122, 117, 146, 206, 111, 110, 135, 130, 124, 153, 136, 112, 118, 97, 154, 217, 275, 180, 121, 129, 119, 138, 127, 181, 98, 137, 150, 188, 183, 185, 4]

for market in loja:
    cursor.execute('SELECT * FROM letter.teste_ped where market = %d limit 0,500;' %(market))


    #INSERT DB lett
    for row in cursor:
        # Query para INSERT
        sql = "INSERT INTO lett.teste_ped (id, datetime, url, name, cat1, cat2, cat3, market, description, html)  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
        cursorLett.execute(sql,valores)

    cnxii.commit()

#Fechar Conexoes
cursor.close()
cursorLett.close()
cnxii.close()
cnxn.close()