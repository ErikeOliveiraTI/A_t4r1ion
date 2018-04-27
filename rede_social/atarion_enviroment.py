import psycopg2
from rede_social.tratamentos import *
from rede_social.Mensagem import Mensagem
import time

class Usuario:
    def __init__(self,nome,idade,profissao):
        self.nome = nome
        self.idade =idade
        self.profissao = profissao

    def get_nome(self):
        return self.nome

    def __str__(self):
        return str(self.nome)+"\n"+str(self.idade)

    def criar_conta(self):
        global conta
        email = input('SEU EMAIL:')
        senha = input("escolha uma senha:")
        conta = Conta(email, senha,)
        return conta

    def logar(self, email, senha):

        if email in sistema.cadastrados.keys():
            if senha in sistema.cadastrados.values():
                conta.logado.append(email)
                conta.login = True
                print("Usuário logado com SUCESSO!")

            else:
                print("senha incorreta")
        else:
            print("Usuário não registrado")
        '''try:
            cursor = sistema.conexao.cursor()
            conta = cursor.execute('SELECT email FROM conta WHERE email=\'{}\''.format(email))
            print(conta)
            while True:
                tupla = cursor.fetchone()  # extrai elemento

                if not tupla:
                    break
                if senha==tupla[1]:
                    conta.logado.append(email)
                    print(conta.logado)
                    conta.login=True
                else:
                    print("senha incorreta !")
            cursor.close()
            sistema.conexao.commit()
            return conta

        except:
            print(' CONTA NÃO ENCONTRADA !!')'''
    def set_idade(self,nova_idade):
        nome = self.get_nome()
        if nova_idade<=15:
            raise IdadeMenorException('ERROR DATA: Idade menor que 15 anos !\n')

        cursor = sistema.conexao.cursor()
        cursor.execute('UPDATE usuario SET idade=(%s) WHERE nome= (%s)',(nova_idade,nome))
        cursor.close()
        sistema.conexao.commit()
        print("idade atualizada !\n")

    def set_nome(self,novo_nome):
        if len(novo_nome)>30:
            raise NomeMaiorexception('ErrorName: Deve ter menos de 30 caracteres !')
        cursor=sistema.conexao.cursor()
        cursor.execute('UPDATE cadastrados SET apelido=(%s) WHERE apelido=(%s)', (novo_nome,self.nome))
        cursor.execute('UPDATE usuario SET nome=(%s) WHERE nome=(%s)',(novo_nome,self.nome))
        cursor.close()
        sistema.conexao.commit()
        #self.nome = novo_nome

    def Logar(self):
        email = conta.email
        senha = conta.senha
        #if email in sistema.get_cadastrados() and senha==sistema.cadastrados[email]:
        conta.login=True
        if email not in conta.logado:
            conta.logado.append(email)
            print("usuario "+email+" entrou !\n")
            #print(conta.logado)
        else:
            print("\t\temail incorreto ou não registrado na rede!\n")



class Conta:
    def __init__(self,email,senha):
        self.email  = email
        self.senha = senha
        self.login = False
        self.logado = []

    def get_email(self):
        return self.email

    def get_dado_email(self):
        return self.email

    def Buscar_amigos(self,nome):
        cursor = sistema.conexao.cursor()
        cursor.execute("SELECT * FROM cadastrados WHERE nome like (%s)",(nome))
        for tupla in cursor.fetchall():
            print('Nome: ' + str(tupla[0]) + ',', 'Email: ' + str(tupla[1]))
        cursor.close()
        sistema.cursor.commit()

    def Adicionar_amigos(self,email):
        usuar=self.adicionar_amigo(email)
        cursor = sistema.conexao.cursor()
        cursor.execute('SELECT * from conta')
        tupla = cursor.fetchall()
        amigo = None
        for e in tupla:
            try:
                if e[0] == email:
                    amigo = e
                    cursor.execute('INSERT INTO amigos(meu_email, nome, email, idade) VALUES (%s, %s, %s, %s)', (conta.email, usuar[0], amigo[1],usuar[1]))
            except :
                if amigo == None:
                    print('Dados do amigo inválidos !')

        cursor.close()
        sistema.conexao.commit()

    def adicionar_amigo(self,email):
        cursor=sistema.conexao.cursor()
        cursor.execute("SELECT * FROM cadastrados WHERE email='"+(email)+"'")
        tupla = cursor.fetchall()

        return tupla

class Grupo:
    def __init__(self,nome, categoria,admin=None):
        self.nome = nome
        self.categoria = categoria
        self.membros =[]


class Administrador(Usuario):
    def __init__(self,codigo):
        Usuario.__init__(self,remetente=None,destino=None)
        self.codigo = codigo

    def criar_grupo(self):
        global grupo
        grupo = Grupo(nome=None,categoria=None,admin=None)


    def add_membro(self,convidado):
        grupo.membros.append(convidado)


class Sistema:
    def __init__(self):
        self.cadastrados = {}
        self.conexao = psycopg2.connect(host="localhost", database="a_tarion", user="postgres", password="123")


    def __str__(self):
        return str(self.cadastrados)

    def Cadastrar_Usuario(self,nome,idade,profissao):
        usr_existe = self.ver_existe_usr()

        if idade<=15:
            raise IdadeMenorException('Caracteres de idade inválidos')
        if len(nome)>=30:
            raise  NomeMaiorexception('Nome muito grande, tente denovo !')

        if usr_existe==nome:
            raise UsuarioExistenteException('Usuario já é membro !')

        cursor = self.conexao.cursor()
        cursor.execute(
            'INSERT INTO usuario(nome, idade,profissao) VALUES (%s, %s, %s)',
            (nome, idade,profissao))

        cursor.close()
        self.conexao.commit()

        global usr
        usr = Usuario(nome,idade,profissao)
        usr.criar_conta()
        self.cadastrar_conta(conta)


    def cadastrar_conta(self, conta):

        email = conta.get_dado_email()

        conta_existe = self.verifica_existe()
        if conta_existe==email:
            raise ContaExistenteException('Esta conta já está cadastrada')

        cursor = self.conexao.cursor()
        cursor.execute(
            'INSERT INTO conta(email, senha) VALUES (%s, %s)',
            (email, conta.senha))
        cursor.execute(
            'INSERT INTO cadastrados(apelido,email) VALUES (%s,%s)', (usr.nome,conta.email)
        )
        self.cadastrados[conta.email] = conta.senha
        print("Usuário adicionado ao sistema com sucesso! "+"\n")
        cursor.close()
        self.conexao.commit()

    def login(self,email,senha):
        cursor = self.conexao.cursor()
        cont=self.get_cadastrados(email)
        if cont:
            cursor.execute('SELECT * FROM conta WHERE email=(%s) and senha=(%s)',(email,senha))
            print("Bem vindo de volta !")
            time.sleep(2)

    def get_cadastrados(self,email):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT email FROM cadastrados WHERE email=\'{}\'".format(email))
        while True:
            tupla = cursor.fetchone() # extrai elemento
            if tupla[0]==email:
                return tupla[0]
        cursor.close()
        self.conexao.commit()
            #return (self.cadastrados)

    def enviar_mensagem(self, mensagem: Mensagem):
        cursor = self.conexao.cursor()
        cursor.execute('INSERT INTO mensagem(escrito, email_r, email_d, data) VALUES (%s, %s, %s, %s)', (mensagem.escrito, mensagem.email_remetente, mensagem.email_destino, mensagem.data))
        cursor.close()
        self.conexao.commit()

    def remover_conta(self):
        c_d=conta.logado
        t = input("Tens a certeza?[S/n]")
        if t=='s':
            cursor=self.conexao.cursor()
            cursor.execute('DELETE FROM cadastrados WHERE email =(%s)', (c_d))
            cursor.execute('DELETE FROM conta WHERE email =(%s)',(c_d))
            cursor.close()
            self.conexao.commit()
        print("conta removida com sucesso, para acessar crie outra conta\n")
        time.sleep(2)

    def Remover_Usuario(self):

        try:
            cursor = self.conexao.cursor()
            cursor.execute('DELETE FROM usuario WHERE nome=\'{}\''.format(usr.get_nome()))
            cursor.close()
            self.conexao.commit()

        except TypeError:
            print("ERRO : DADOS SEM FUNDO!")



    def set_senha(self, email):
        senha_antig = input("informe a senha atual:")
        if senha_antig == self.cadastrados[email]:
            senha_nova = input("informe a senha nova:")
            cursor= self.conexao.cursor()
            cursor.execute('UPDATE conta SET senha=(%s) WHERE email=(%s)',(senha_nova,email))
            cursor.close()
            self.conexao.commit()
            self.cadastrados[email] = senha_nova
            print("Pronto, agora sua conta estará mais segura!"+"\n")
            print(self.cadastrados)
        else:
            print("dados inválidos!")
    def ver_existe_usr(self):
        cursor = self.conexao.cursor()
        cursor.execute('SELECT nome FROM usuario')
        while True:
            tupla = cursor.fetchone()  # extrai elemento

            if not tupla:
                break
            return (tupla[0])
        cursor.close()
        self.conexao.commit()

    def verifica_existe(self):

        cursor = self.conexao.cursor()
        cursor.execute('SELECT * FROM conta')
        while True:
            tupla = cursor.fetchone()  # extrai elemento

            if not tupla:
                break
            return (tupla)
        cursor.close()
        self.conexao.commit()

    def __montar_objeto_conta(self,tupla):
        #atributos = self.verifica_existe()
        return Conta(tupla[0],tupla[1])

    def __montar_objeto_mensagem(self,tupla):
            # atributos = self.verifica_existe()
        return Mensagem(tupla[0], tupla[1],tupla[2])


    def main_conta(self):
        while True:


            print('\tr - Remover conta')
            print('\ti - atualizar Informacao')
            print("\te - Enviar mensagem")
            print("\tb - Buscar Amigo")
            print('\to - Sair(o)')
            opcao = input("sua escolha:")
            if opcao == 'r':
                self.remover_conta()
                self.Remover_Usuario()
                break
            if opcao=='i':
                print("\t\ts - trocar Senha")
                print("\t\tn - trocar Nome")
                print("\t\ti - mudar Idade")
                info = input("Tu desejas?")
                if info=='s':
                    email = input("informe o seu email:")
                    '''if email in conta.logado:
                        self.set_senha(email)
                    else:
                        print("\nvoce deve entrar com esta conta!\n")'''
                    self.set_senha(email)
                if info=='n':
                    novo_nome = input("Como você quer ser chamado?")
                    usr.set_nome(novo_nome)
                    print("VOCÊ AGORA É CONHECIDO COMO ",usr.nome)
                    time.sleep(3)
                if info=='i':
                    nova_idade = int(input("nova idade:"))
                    usr.set_idade(nova_idade)
            if opcao=='e':
                escrito=input("escrito")
                email_r=conta.email
                email_d=input("destino:")

                mensagem=Mensagem(escrito,email_r,email_d)
                self.enviar_mensagem(mensagem)

            if opcao=='b':
                try:
                    bc=input("POR:"
                          "\temail(e)\n"
                          "\tnome(n)\n"
                          "tu escolhes?")
                    if bc=='e':
                        email = input("Qual o email desta pessoa?")
                        sistema.get_cadastrados(email)
                    if bc=='n':
                        nome=input("qual o nome desta pessoa?")
                        conta.Buscar_amigos(nome)
                    op = input("quer adicionar como amigo?[s/n]")
                    if op == 's':
                        conta.Adicionar_amigos(email)
                        print("Amigo adicionado !")
                        time.sleep(2)
                except ContaExistenteException:
                    print("Email não existente !\n")

            if opcao=='o':
                print("Você saiu !")
                time.sleep(2)
                self.menu()

    def menu(self):
        while True:
            print("\n+----------------------------+\n")
            print("| SEJA BEM VINDO AO A_TARION |")
            print("\n+----------------------------+\n")
            print("\t\tE - Entrar")
            print("\t\tR - Registrar-se")
            print("\t\tS - Sair")

            esc = input("tua opcao:").lower()
            if esc=="r":
                try:
                    nome = input("informe seu nome:")
                    idade = int(input("sua idade:"))
                    profissao = input("qual a sua profissao?")
                    self.Cadastrar_Usuario(nome,idade, profissao)
                    usr.Logar()
                    self.main_conta()

                except IdadeMenorException as m:
                    print("Erro:",m)
                    time.sleep(3)
                except ContaExistenteException as c:
                    print("Erro:",c)
                    time.sleep(3)
                except NomeMaiorexception as nm:
                    print("ERRO:",nm)
                    time.sleep(3)
                except UsuarioExistenteException as usr_e:
                    print("ERRO: ",usr_e)
                    time.sleep(3)

            if esc=="e":

                email = input("Teu email no atarion:\n")
                senha = input("Tua senha:\n")  ##colocar variáveis no sistema
                self.login(email,senha)
                tupla=self.verifica_existe()
                conta = self.__montar_objeto_conta(tupla)
                global conta
                self.cadastrados[email]=senha
                self.main_conta()
                return conta
                #self.verifica_existe()


            if esc=="s":
                print("\n>>> OBRIGADO POR UTILIZAR O A_TARION! <<<\n")
                break



sistema = Sistema()
#sistema.menu()
