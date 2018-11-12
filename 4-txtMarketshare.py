#Conexao com base de dados
import pymysql
import copy

from requests import get
from bs4 import BeautifulSoup

#Argumentos para estabelecer conexao com o banco de dados MySql SELECT
cnxn = pymysql.connect(host='localhost', db='stage_lett', user='root', passwd='123456')
#Atribuicao para conexao
cursor = cnxn.cursor()
#Query para coleta de Dados


#Query para coleta de Dados
#Total por marcas, agrupados por supermercado
cursor.execute('select market, brand, count(brand)  from stage_lett.produto  group by market,brand  order by market;')
tMarcas = copy.copy(cursor)
cursor.execute('select market, count(market)  from stage_lett.produto  group by market  order by market;')
tMarket = copy.copy(cursor)

#Salvando as notas em um arquivo de texto
file = open('marketshare.txt', 'w')

for row in tMarcas:
    #Tratamento das strings
    strMarca = str(row[1]).replace('desconhecid','desconhecida')\
        .replace('semptoshib', 'semp toshiba')\
        .replace('semptcl','semp toshiba')\
        .replace('lgeletronics','lg')\
        .replace('otorol','motorola').replace('mmotorolaa','motorola')\
        .replace('ide','midea').replace('mideaa','midea').replace('mmidea','midea')\
        .replace('springermmidea','midea').replace('springermidea','springer midea')\
        .replace('hphewlettpackard','hp')\
        .replace('noinformado','nao informado')\
        .replace('panasoni','panasonic').replace('panasonicc', 'panasonic')\
        .replace('mideacarrier','midea carrier')\
        .replace('olimpiasplendid','olimpia splendid')\
        .replace('springe','springer').replace('springerr','springer')\
        .replace('lgseminovos','lg')\
        .replace('springercarrier','springer carrier')\
        .replace('samsungseminovos','samsung')\
        .replace('hpbrasil','hp')\
        .replace('passebem','passe bem')\
        .replace('editorapositivo','positivo')\
        .replace('ace','acer').replace('acerr','acer')\
        .replace('hbmveis','hb moveis')\
        .replace('carrie','carrier').replace('carrierr','carrier')\
        .replace('mideacarrier', 'midea carrier')\
        .replace('paracapitaiseregiesmetropolitanas ','desconhecida')\
        .replace('sacprobelcolchoesindb','desconhecida')\
        .replace('paraasdemaislocalidades','desconhecida')\
        .replace('atendimentoaoclientecapitaisegrandescentros', 'desconhecida')\
        .replace('paracapitaiseregiesmetropolitanas','desconhecida')\
        .replace('capacidadedapilhaoubateri','desconhecida')\
        .replace('garantiadofornecedo','desconhecida')\
        .replace('itensinclusos','desconhecida')


    for rowMarket in tMarket:
        if rowMarket[0] == row[0]:
            totalMarket = rowMarket[1]
            break

    marketShare = row[2] * 100 / rowMarket[1]

    line = ('%s = %s = %s %% \n' %(strMarca,row[0],marketShare))

    #write line
    file.write(line)

#Fechar Conexoes
cursor.close()
cnxn.close()
file.close()