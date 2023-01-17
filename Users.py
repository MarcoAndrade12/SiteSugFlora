import Defs as df
import color as col
import log

################## Criação e edição dos usuários

###### read(): f() Lê o banco de dados user.txt e retorna uma lista com todos os usuários: users = [[Login,Nome,Senha],[Login,Nome,Senha]](exemplo)
def read(): #definindo a função read()
    while True:
        try:
            user= open('usuarios.txt','r') #abrindo o txt
            L1=[] #criando lista em branco
            for i in user: 
                L1.append(i.rstrip('\n').split(',')) #adiocionando o txt na lista L1, retirando o \n e colocando a vírgula para separar
                
            return L1 #retornando a lista L1
            
        except:
            user= open('usuarios.txt','a')
            user.write('ID, Nome, Login, Senha')

###### verId(): f(id) Verifica no banco de dados user.txt se o Id existe entre os usuários.
def verId(id): #Definindo a função verId()
    lista = read() #implementando na variavel lista a função read
    for i in lista: #passando pela lista

        if id == str(i[0]): #se já houver o id na lista retorna como 1 e se não houver retorna como 0
            return 1
    
    return 0 #retorna 0 caso não haja o id na lista

###### Login: f(login,senha) Verifica se o usuário existe no banco de dados user.txt e retorna False se não tiver ou uma lista = [Login,Nome,Senha]
def login(Login,Senha): #definindo a função login()

    users = read() #verifica a lista dos usuários e retorna com os dados implementando na variavel users

    logg = [user for user in users if Login == str(user[2]) and Senha == str(user[3])] #verificando se os dados de login, nome e senha já estão no banco de dados

    if logg == []: #Se os dados não estiverem na lista ele retorna como false
        return False
    else:
        return logg[0] #se os dados estiverem na lista retorna uma lista com os dados do usuário

###### NewUser: f(login,nome,senha) Novo usuário
            #OBS: Não esquecer de utilizar o df.NextId(read()) para saber qual é o próximo ID do usuário.
def cadastro_cliente(nome,login,senha): #definindo a função cadastro_cliente()
    bd=open("usuarios.txt","a") #abre o banco de dados com os dados dos usuários
    L1=[] #cria uma lista vazia
    if nome == '' or login == '' or senha =='': #se o usuário não acrescentar nada ao fazer o cadastro, retorna como falso
        return False

    L1.append(df.NextId(read())) #adiciona no banco de dados na próxima linha um novo id para o usuário que está criando o cadastro   
    L1.append(nome) #adiciona no banco de dados o nome do usuário que está se cadastrando
    L1.append(login) #adiciona no banco de dados o login do usuário que está se cadastrando
    L1.append(senha) #adiciona no banco de dados a senha do usuário que está se cadastrando
    
    registro = '\n' + str(L1[0]) + ',' + L1[1] + ',' + L1[2] + ',' + str(L1[3]) #transformando o id e a senha do usuário cadastrado em string, fazendo a separação com virgula e pulando linha
    
    bd.write(registro) #grava no banco de dados as informações passadas anteriormente

    return read() #retorna a função read
    
###### EditUser: f(id) Para editar o usuário já existente.
            #OBS: Não esquecer de fazer a verificação se o usuário existe e retornar None caso o usuário não exista.

###### DelUser: f(id) Para excluir o usuário já existente.
            #OBS: Não esquecer de fazer a verificação se o usuário existe e retornar None caso o usuário não exista.
