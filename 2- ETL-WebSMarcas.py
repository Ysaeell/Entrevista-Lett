#Conexao com base de dados
import pymysql
from bs4 import BeautifulSoup
# Importar biblioteca de Expressao regular
import re
# Importaçao para fazer o get
# from requests import get

#Argumentos para estabelecer conexao com o banco de dados SqlServer
cnxn = pymysql.connect(host='localhost', db='letter', user='root', passwd='123456')

#Atribuicao para conexao
cursor = cnxn.cursor()
#Query para coleta de Dados
cursor.execute('SELECT html, id, market FROM lett.teste_ped;')

#Argumentos para estabelecer conexao com o banco de dados MySql INSERT
cnxii = pymysql.connect(host='localhost', db='stage_lett', user='root', passwd='123456')
#Atribuicao para conexao
cursorLett = cnxii.cursor()

#variaveis usadas
notes = []
contador = int(0)

#codigo HTML esta sendo retirado do row[0]

for row in cursor:
    html_soup = BeautifulSoup(row[0], 'html.parser')
	
	#IDs *market id*-->
    #58,73,206,62,63,
    notes_containers = html_soup.find_all('strong', class_='brand')

    #ERROS na coleta - foram tratados

    #136
    if row[2] == 136:
        notes_containers = html_soup.find_all('span', itemprop='name')
        notes = notes_containers
        try:
            notes_containers = BeautifulSoup(str(notes[1]), 'html.parser')
        except:
            notes_containers = BeautifulSoup("<a>desconhecida</a>", 'html.parser')
            continue

    if row[2] == 174:
        notes_containers = BeautifulSoup("<a>desconhecida</a>",'html.parser')

    if row[2] == 109:
        notes_containers = BeautifulSoup("<a>desconhecida</a>",'html.parser')

    if row[2] == 97:
        #Pagina gerada por codigo html
        notes_containers = BeautifulSoup("<a>desconhecida</a>", 'html.parser')

        #Pagina com erro de Identaçao#
        #notes_containers = html_soup.find_all('div', class_='product-title-info')
    if row[2] == 217:
        #processamento com excesso de espaço
        notes_containers = html_soup.find_all('div', class_='brand-sem-logo')

    if row[2] == 121:
        notes_containers = html_soup.find_all('a', itemprop="brand")

    if row[2] == 137:
        notes_containers = BeautifulSoup("<a>desconhecida</a>",'html.parser')

    #188
    if row[2] == 188:
        notes_containers = html_soup.find_all('span', itemprop='brand')

    if row[2] == 183:
        notes_containers = BeautifulSoup("<a>desconhecida</a>",'html.parser')

    if row[2] == 185:
        notes_containers = html_soup.find_all('div', class_='brandProduct')

    # 118
    if row[2] == 118:
        notes_containers = html_soup.find_all('div', class_='caracteristicas-fabricante-item')
        try:
            notes = notes_containers[0]
        except:
            notes = '<a>desconhecida</a>'
            continue
        html_soup = BeautifulSoup(str(notes), 'html.parser')
        notes_containers = html_soup.find_all('span')

    #ROTINAS PARA TABLE

    #A url envia para uma pagina feita em Java Script que gera o HTML, pagina baseada em JavaScript
    ''' CODIGO NAO IMPLEMENTADO, necessario acrescenta (url) a query 
    # 124 WEB
    if row[2] == 124:
        #Passando Html
        url = get(str(row[3]))

        #verificando o recebimento
        if url.status_code != 200:
            notes_containers = BeautifulSoup("<a>desconhecida</a>", 'html.parser')
            break

        html_soup = BeautifulSoup(url.text, 'html.parser')

        notes_containers = html_soup.find_all('div', class_='linha spec')
        notes = notes_containers
        html_soup = BeautifulSoup(str(notes), 'html.parser')
        notes_containers = html_soup.find_all("tr")
        notes = notes_containers

        for tr in notes:
            html_soup = BeautifulSoup(str(tr), 'html.parser')
            notes_containers = html_soup.find_all('td')
            notes = notes_containers[1]
            esc = BeautifulSoup(str(notes_containers[0]), 'html.parser').text
            if esc == 'Marca':
                notes_containers = BeautifulSoup(str(notes), 'html.parser')
                break
        '''

    # 180
    if row[2] == 180:
        notes_containers = html_soup.find_all('table', class_='data-table product-additional-info')
        notes = notes_containers
        html_soup = BeautifulSoup(str(notes), 'html.parser')
        notes_containers = html_soup.find_all('tr')
        notes = notes_containers

        for tr in notes:
            html_soup = BeautifulSoup(str(tr), 'html.parser')
            try:
                notes_containers = html_soup.find_all('th')
                esc = str(notes_containers[0].text)
            except:
                notes_containers = BeautifulSoup("<a>desconhecida</a>", 'html.parser')
                continue


            if esc == 'Marca':
                html_soup = BeautifulSoup(str(tr), 'html.parser')
                notes_containers = html_soup.find_all('td')
                break

    # 165
    if row[2] == 165:
        notes_containers = html_soup.find_all('div', class_='panel-group')
        notes = notes_containers
        html_soup = BeautifulSoup(str(notes), 'html.parser')
        notes_containers = html_soup.find_all('tr')
        notes = notes_containers

        for tr in notes:
            html_soup = BeautifulSoup(str(tr), 'html.parser')
            notes_containers = html_soup.find_all('td')
            try:
                notes = notes_containers[1]
                esc = BeautifulSoup(str(notes_containers[0]), 'html.parser').text
            except:
                notes_containers = BeautifulSoup("<a>desconhecida</a>", 'html.parser')
                continue

            if esc == 'Marca':
                notes_containers = BeautifulSoup(str(notes), 'html.parser')
                break
    # 59, 60
    if row[2] == 59 or row[2] == 60:
        notes_containers = html_soup.find_all('table', class_='table table-striped')
        notes = notes_containers
        html_soup = BeautifulSoup(str(notes), 'html.parser')
        notes_containers = html_soup.find_all("tr")
        notes = notes_containers

        for tr in notes:
            html_soup = BeautifulSoup(str(tr), 'html.parser')
            notes_containers = html_soup.find_all('td')
            try:
                notes = notes_containers[1]
                esc = BeautifulSoup(str(notes_containers[0]), 'html.parser').text
            except:
                notes_containers = BeautifulSoup("<a>desconhecida</a>", 'html.parser')
                continue
            if esc == 'Marca':
                notes_containers = BeautifulSoup(str(notes), 'html.parser')
                break

    #61
    if row[2] == 61:
        notes_containers = html_soup.find_all('table', class_='table table-striped')
        notes = notes_containers
        html_soup = BeautifulSoup(str(notes), 'html.parser')
        notes_containers = html_soup.find_all("tr")
        notes = notes_containers

        for tr in notes:
            html_soup = BeautifulSoup(str(tr), 'html.parser')
            #caso a variavel receber 3 colunas ou uma tag com colspan
            try:
                notes_containers = html_soup.find_all('td')
                notes = notes_containers[1]
            except:
                notes_containers = BeautifulSoup("<a>desconhecida</a>", 'html.parser')
                continue
            esc = BeautifulSoup(str(notes_containers[0]), 'html.parser').text
            if esc == 'Marca':
                notes_containers = BeautifulSoup(str(notes), 'html.parser')
                break
    # 174
    if row[2] == 174:
        notes_containers = html_soup.find_all('div', class_='dsc-block carac-principais-container')
        notes = notes_containers
        html_soup = BeautifulSoup(str(notes), 'html.parser')
        notes_containers = html_soup.find_all("tr")
        notes = notes_containers

        for tr in notes:
            html_soup = BeautifulSoup(str(tr), 'html.parser')
            try:
                notes_containers = html_soup.find_all('td')
                notes = notes_containers[2]
            except:
                notes_containers = BeautifulSoup("<a>desconhecida</a>", 'html.parser')
                continue

            esc = BeautifulSoup(str(notes_containers[1]), 'html.parser').text
            if esc == 'Fabricante':
                notes_containers = BeautifulSoup(str(notes), 'html.parser')
                break
    #94
    if row[2] == 94:
        notes_containers = html_soup.find_all('div', class_='produto-descricao-caracteristicas')
        notes = notes_containers
        html_soup = BeautifulSoup(str(notes), 'html.parser')
        notes_containers = html_soup.find_all("tr")
        notes = notes_containers

        for tr in notes:
            html_soup = BeautifulSoup(str(tr), 'html.parser')
            notes_containers = html_soup.find_all('td')
            try:
                notes = notes_containers[1]
                esc = BeautifulSoup(str(notes_containers[0]), 'html.parser').text
            except:
                continue
            if esc == 'Marca':
                notes_containers = BeautifulSoup(str(notes), 'html.parser')
                break
            notes_containers = BeautifulSoup("<a>desconhecida</a>", 'html.parser')

    # 122
    if row[2] == 122:
        notes_containers = html_soup.find_all('div', id='tabs-produto')
        notes = notes_containers
        html_soup = BeautifulSoup(str(notes), 'html.parser')
        notes_containers = html_soup.find_all("tr")
        try:
            tr = notes_containers[1]

            #Pega a segunda linha da tabela//Estaticamente
            html_soup = BeautifulSoup(str(tr), 'html.parser')
            notes_containers = html_soup.find_all('td')
            notes = notes_containers[2]
        except:
            notes_containers = BeautifulSoup("<a>desconhecida</a>", 'html.parser')
            continue

        esc = BeautifulSoup(str(notes_containers[1]), 'html.parser').text
        if esc == 'Marca:':
            notes_containers = BeautifulSoup(str(notes), 'html.parser')
        else:
            notes_containers = BeautifulSoup("<a>desconhecida</a>", 'html.parser')

    # 137
    if row[2] == 137:
        notes_containers = html_soup.find_all('table', class_='data-table table')
        notes = notes_containers
        html_soup = BeautifulSoup(str(notes), 'html.parser')
        notes_containers = html_soup.find_all("tr")
        notes = notes_containers

        for tr in notes:
            html_soup = BeautifulSoup(str(tr), 'html.parser')
            notes_containers = html_soup.find_all('th')
            try:
                esc = str(notes_containers[0].text)
            except:
                notes_containers = BeautifulSoup("<a>desconhecida</a>", 'html.parser')
                continue


            if esc == 'FABRICANTE':
                html_soup = BeautifulSoup(str(tr), 'html.parser')
                notes_containers = html_soup.find_all('td')
                break

    #Filtro sem table
    # 146
    if notes_containers == []:
        notes_containers = html_soup.find_all('a', class_='prd-brand')

    #117
    if notes_containers == []:
        notes_containers = html_soup.find_all('td', class_='x-brand')

    #131
    if notes_containers == []:
        notes_containers = html_soup.find_all('div', class_='item opcaoProcurarMais')
        if notes_containers != []:
            html_soup = BeautifulSoup(str(notes_containers), 'html.parser')
            notes_containers = html_soup.find_all('span')
            notes = notes_containers
            try:
                notes_containers = BeautifulSoup(str(notes[1]), 'html.parser')
            except:
                notes_containers = BeautifulSoup("<a>desconhecida</a>", 'html.parser')
                continue

    if notes_containers == []:
        notes_containers = html_soup.find_all('a', class_='product-brand')

    #134,135,153
    if notes_containers == []:
        notes_containers = html_soup.find_all('div', id='brand')

    #159,120,150
    if notes_containers == []:
        notes_containers = html_soup.find_all('td', class_='value-field Marca')

    #162
    if notes_containers == []:
        notes_containers = html_soup.find_all('div', class_='flix-headline')

    #111,138,181
    if notes_containers == []:
        notes_containers = html_soup.find_all('a', class_='brand')

    #113
    if notes_containers == []:
        notes_containers = html_soup.find_all('span', itemprop='name')

    #133,119
    if notes_containers == []:
        notes_containers = html_soup.find_all('td', class_='value-field Modelo-Ar-Condicionado')

    #132
    if notes_containers == []:
        notes_containers = html_soup.find_all('td', class_='value-field Fabricante')


    #101
    if notes_containers == []:
        notes_containers = html_soup.find_all('div', class_='brand-name')
        if notes_containers != []:
            html_soup(notes_containers)
            notes_containers = html_soup.find_all('a')

    #125
    if notes_containers == []:
        notes_containers = html_soup.find_all('div', class_='prd-small-info-brand')
        if notes_containers != []:
            html_soup(notes_containers)
            notes_containers = html_soup.find_all('a')

    #182 (Pagina com erro de identaçao)
    if notes_containers == []:
        notes_containers = html_soup.find_all('div', class_='manufacturers')
        if notes_containers != []:
            html_soup(notes_containers)
            #Passa a pagina para o notes para separa os textos encontrados nas tags "span"
            notes = html_soup.find_all('span', class_='value')
            try:
                notes_containers = BeautifulSoup(str(notes[0]), 'html.parser')
            except:
                notes_containers = BeautifulSoup("<a>desconhecida</a>", 'html.parser')
                continue

    # 110
    if notes_containers == []:
        notes_containers = html_soup.find_all('h2', class_='brand livedata')

    # 112
    if notes_containers == []:
        notes_containers = html_soup.find_all('a', class_='marca-product')

    # 275
    if notes_containers == []:
        notes_containers = html_soup.find_all('li', itemprop='brand')

    # 127
    if notes_containers == []:
        notes_containers = html_soup.find_all('div', class_='marca')
        notes = notes_containers
        html_soup = BeautifulSoup(str(notes), 'html.parser')
        notes_containers = html_soup.find_all('span')

        #Caso nao encontre retorna como desconhecida
    if notes_containers == []:
        notes_containers = BeautifulSoup("<a>desconhecida</a>",'html.parser')

    for container in notes_containers:
        #tratamento
        strMarca = container.text.strip("\n").strip("Marca:").strip()
        strMarca = re.sub('[^aA-zZ,]', '', strMarca).lower()

        #query sql
        valores = (row[1], str(strMarca), row[2])
        sql = "INSERT INTO stage_lett.produto (idprod, brand, market)  VALUES (%s, %s, %s)"

        try:
            cursorLett.execute(sql, valores)
        except:
            continue
    cnxii.commit()

    contador += 1
    print("%d" % (contador * 100 / 18647))

#Fechar Conexoes
cursor.close()
cnxn.close()

#'''END'''