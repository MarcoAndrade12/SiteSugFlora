import bd_coletas as bd
import log
#Usado para pesquisa com algum termino unico usado pelo usuario

def pesquisa (pesquisa,bd):
    coleta=[coleta for coleta in bd if str(pesquisa) in coleta]
    return coleta

def pesquisafiltro (pesquisafiltro,bd):
    newBd = []

    for coleta in bd:
        for crit in pesquisafiltro:
            if crit in coleta and coleta not in newBd:
                newBd.append(coleta)
    return newBd

#---- Funções----#
# RELATÓRIOS QUANTITATIVOS

# Victor # Frequência de familia/Genero/Espécie > Retorna a quantidade de vezes que aquele critério aparece = Total dele dividido pelo total de coletas.    
def freq(bd,critério):
    try:
        filtro = len([freq for freq in bd if critério in freq])
        coletas = len(bd)-1
        if filtro > 0:
            freq = filtro / coletas
        else:
            freq = 0.0 
            log.NewLog('Pesquisa.freq',f'A consulta da frequência de "{critério}" retornou 0.0. Ou sua escrita está errada, ou realmente não existe no banco de dados.')
        return freq
    except:
        log.NewLog('Pesquisa.freq',f'Erro ao tentar retornar a frequência do critério "{critério}". Provavelmente ele não existe no banco de dados fornecido para a função ou sua escrita está errada ou o banco de dados está em branco.')
        
        return False

    # Stephanie # Total de coletas identificadas para cada critério.
def identificadosfiltro(criterio,bd): #criando função e declarando como parametros criterio e bd
    bd= pesquisa(criterio,bd) #variavel bd realizara uma pesquisa em critério e bd
    coleta= [] #criando lista vazia 
    for co in bd: #passando por todos os itens do bd
        if co[3] != "N/Id" and co[4] != 'N/Id' and co[5] != 'N/Id': #Verificando se algum item das posições 3,4 e 5 do bd não conter 'N/Id'
            coleta.append(co) #os itens identificados acima serão inseridos na lista coleta
    return coleta #retornando coleta

def identificados(bd): #criando função e declarando como parametros criterio e bd
    coleta= [] #criando lista vazia 
    for co in bd: #passando por todos os itens do bd
        if co[3] != "N/Id" and co[4] != 'N/Id' and co[5] != 'N/Id': #Verificando se algum item das posições 3,4 e 5 do bd não conter 'N/Id'
            coleta.append(co) #os itens identificados acima serão inseridos na lista coleta
    return coleta #retornando coleta

    # Stephanie # Total de coletas não identificadas para cada critério.

def Nidentificadosfiltro(criterio,bd): #criando função e declarando como parametros criterio e bd
    bd= pesquisa(criterio,bd) #variavel bd realizara uma pesquisa em critério e bd
    coleta= [] #criando lista vazia 
    for co in bd: #passando por todos os itens do bd
        if co[3] == "N/Id" or co[4] == 'N/Id' or co[5] == 'N/Id': #Verificando se algum item das posições 3,4 e 5 do bd contém 'N/Id'
            coleta.append(co) #os itens identificados acima serão inseridos na lista coleta
    return coleta 

def Nidentificados(bd): #criando função e declarando como parametros criterio e bd
    coleta= [] #criando lista vazia 
    for co in bd: #passando por todos os itens do bd
        if co[3] == "N/Id" or co[4] == 'N/Id' or co[5] == 'N/Id': #Verificando se algum item das posições 3,4 e 5 do bd contém 'N/Id'
            coleta.append(co) #os itens identificados acima serão inseridos na lista coleta
    return coleta 

def FNidentificados(bd): #criando função e declarando como parametros criterio e bd
    coleta= [] #criando lista vazia 
    for co in bd: #passando por todos os itens do bd
        if co[3] == "N/Id": #Verificando se algum item das posições 3,4 e 5 do bd contém 'N/Id'
            coleta.append(co) #os itens identificados acima serão inseridos na lista coleta
    return coleta 

def GNidentificados(bd): #criando função e declarando como parametros criterio e bd
    coleta= [] #criando lista vazia 
    for co in bd: #passando por todos os itens do bd
        if co[3] == "N/Id" or co[4] == 'N/Id': #Verificando se algum item das posições 3,4 e 5 do bd contém 'N/Id'
            coleta.append(co) #os itens identificados acima serão inseridos na lista coleta
    return coleta 

def ENidentificados(bd): #criando função e declarando como parametros criterio e bd
    coleta= [] #criando lista vazia 
    for co in bd: #passando por todos os itens do bd
        if co[3] == "N/Id" or co[4] == 'N/Id' or co[5] == 'N/Id': #Verificando se algum item das posições 3,4 e 5 do bd contém 'N/Id'
            coleta.append(co) #os itens identificados acima serão inseridos na lista coleta
    return coleta     

def Fidentificados(bd): #criando função e declarando como parametros criterio e bd
    coleta= [] #criando lista vazia 
    for co in bd: #passando por todos os itens do bd
        if co[3] != "N/Id": #Verificando se algum item das posições 3,4 e 5 do bd não conter 'N/Id'
            coleta.append(co) #os itens identificados acima serão inseridos na lista coleta
    return coleta #retornando coleta

def Gidentificados(bd): #criando função e declarando como parametros criterio e bd
    coleta= [] #criando lista vazia 
    for co in bd: #passando por todos os itens do bd
        if co[3] != "N/Id" and co[4] != 'N/Id': #Verificando se algum item das posições 3,4 e 5 do bd não conter 'N/Id'
            coleta.append(co) #os itens identificados acima serão inseridos na lista coleta
    return coleta #retornando coleta

def Eidentificados(bd): #criando função e declarando como parametros criterio e bd
    coleta= [] #criando lista vazia 
    for co in bd: #passando por todos os itens do bd
        if co[3] != "N/Id" and co[4] != 'N/Id'  and co[5] != 'N/Id' : #Verificando se algum item das posições 3,4 e 5 do bd não conter 'N/Id'
            coleta.append(co) #os itens identificados acima serão inseridos na lista coleta
    return coleta #retornando coleta

# RELATÓRIOS ESTATÍSTICOS
    
    # Robson # Quantidade de coletas totalmente identificadas em % > Conta quantas coletas estão 100% identificadas e divide pela quantidade de coletas totais
    # Robson # Quantidade de coletas em % para um critério > Conta quantas coletas de um critério estão 100% identificadas e divide pela quantidade de coletas totais

