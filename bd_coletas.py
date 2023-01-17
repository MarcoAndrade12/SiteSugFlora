#banco de dados
#leitura
import Defs as df
import log

def read(ID_user):
    ID_user = str(ID_user)
    # Abre o banco de dados das coletas e retorna ao programador uma lista contendo todas as coletas.
    # Retorna junto o cabeçalho do arquivo.txt se tiver.
    while True:
        try:
            coletas=open("coletas.txt","r")
            
                # Abre o arquivo em modo de leitura e armazena ele na variável coleta
            lista_all=[]
                # Cria uma lista temporária para armazenar uma lista com as coletas
            for i in coletas:
                # Passa dentro de coletas e pega cada uma das linhas em formato string

                coleta = i.strip("\n").split(",")
                
                if str(coleta[1]) == ID_user:
                    lista_all.append(coleta)
                    # Transforma a string da linha em uma lista e retira o caractere especial \n
                    
            # log.NewLog('bd_coletas.read',lista_all)
            return lista_all
                # Retorna ao programador que chamou a função, uma lista com todas as coletas do arquivo.txt
        except:
            coletas = open('coletas.txt','a')
            coletas.write('ID,ID_user,Data,familia,genero,especie,habito,origem,recursos,referencia,floração')

def readall():
  
    # Abre o banco de dados das coletas e retorna ao programador uma lista contendo todas as coletas.
    # Retorna junto o cabeçalho do arquivo.txt se tiver.

    coletas=open("coletas.txt","r")
    
        # Abre o arquivo em modo de leitura e armazena ele na variável coleta
    lista_all=[]
        # Cria uma lista temporária para armazenar uma lista com as coletas
    for i in coletas:
        # Passa dentro de coletas e pega cada uma das linhas em formato string
        coleta = i.strip("\n").split(",")
        lista_all.append(coleta)
        # Transforma a string da linha em uma lista e retira o caractere especial \n

    return lista_all
        # Retorna ao programador que chamou a função, uma lista com todas as coletas do arquivo.txt

#insert
def insert(ID_user,coleta):
    # Função para inserir apenas UMA coleta no banco de dados.
    bd=open("coletas.txt","a")
        # abre o arquivo coletas.txt em modo append
    registro = "\n" + str(df.NextId(readall())) + ',' + ID_user + "," + coleta
        # Cria um registro que será armazenado como nova coleta
        # Se trata de uma string na estrutura que nosso banco de dados exige
        # Antes, ele procura qual o próximo Id da coleta a ser inserida e coloca junto da string.
    bd.write(registro)
        # Escreve a nova coleta no banco de dados na próxima linha do arquivo.
    return read(ID_user) 
        # Faz novamente a leitura do banco de dados atualizado e retorna a nova versão.

def editar(newColeta):

    arqAntigo = readall()
    
    Id = str(newColeta[0])

    for index, coleta in enumerate(arqAntigo):
        if str(coleta[0]) == Id:
            arqAntigo[index] = newColeta
            break
    
    newArq = open('coletas.txt','w')

    arqAntigo = '\n'.join(map(str,arqAntigo)).replace('[','').replace(']','').replace("'",'').replace(" ","")
    
    newArq.write(arqAntigo)

def excluir(ID_Coleta):
    arqAntigo = readall()

    for index, coleta in enumerate(arqAntigo):
        if str(coleta[0]) == ID_Coleta:
            arqAntigo.pop(index)
            break
    
    newArq = open('coletas.txt','w')

    arqAntigo = '\n'.join(map(str,arqAntigo)).replace('[','').replace(']','').replace("'",'').replace(" ","")
    
    newArq.write(arqAntigo)
