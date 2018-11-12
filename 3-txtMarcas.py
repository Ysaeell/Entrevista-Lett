#Conexao com base de dados
import pymysql

from requests import get
from bs4 import BeautifulSoup

#Argumentos para estabelecer conexao com o banco de dados MySql SELECT
cnxn = pymysql.connect(host='localhost', db='stage_lett', user='root', passwd='123456')
#Atribuicao para conexao
cursor = cnxn.cursor()
#Query para coleta de Dados


#Query para coleta de Dados
cursor.execute('SELECT idprod, brand FROM stage_lett.produto;')

#Salvando as notas em um arquivo de texto
file = open('marcas.txt', 'w')

for row in cursor:
    #Tratamento das strings
    strMarca = str(row[1]).replace('desconhecid','desconhecida')\
        .replace('semptoshib', 'semp toshiba')\
        .replace('semptcl','semp toshiba')\
        .replace('lgeletronics','lg')\
        .replace('otorol','motorola').replace('mmotorolaa','motorola')\
        .replace('ide','midea').replace('mideaa','midea').replace('mmidea','midea')\
        .replace('springermmidea','midea')\
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
        .replace('mideacarrier', 'midea carrier') \
        .replace('paracapitaiseregiesmetropolitanas ', 'desconhecida') \
        .replace('sacprobelcolchoesindb', 'desconhecida') \
        .replace('paraasdemaislocalidades', 'desconhecida') \
        .replace('atendimentoaoclientecapitaisegrandescentros', 'desconhecida') \
        .replace('paracapitaiseregiesmetropolitanas', 'desconhecida') \
        .replace('capacidadedapilhaoubateri', 'desconhecida') \
        .replace('garantiadofornecedo', 'desconhecida') \
        .replace('itensinclusos', 'desconhecida')

    line = ('%s = %s\n' %(row[0],strMarca))

    file.write(line)



#Fechar Conexoes
cursor.close()
cnxn.close()
file.close()