from tratamentos import *
import psycopg2

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
        conta = Conta(email, senha,usr)
        return conta

    def logar(self, email, senha):
        if email in sistema.cadastrados.keys():
            if senha in sistema.cadastrados.values():
                conta.logado.append(email)
                conta.login = True
                print("Usuário logado !")

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
        sistema.get_cadastrados()
        #if email in sistema.get_cadastrados() and senha==sistema.cadastrados[email]:
        conta.login=True
        if email not in conta.logado:
            conta.logado.append(email)
            print("usuario "+email+" entrou !\n")
            #print(conta.logado)
        else:
            print("\t\temail incorreto ou não registrado na rede!\n")



class Conta:
    def __init__(self,email,senha,usr):
        self.email  = email
        self.senha = senha
        self.amigos = []
        self.login = False
        self.logado = []

    def get_email(self):
        return self.email

    def get_dado_email(self):
        return self.email

    def add_friend(self):
        amg= input("procurar nick:")
        if amg==usr.nome:
            self.amigos.append(usr)
            print(self.amigos)


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

from datetime import datetime
hoje = datetime.now()

class Mensagem:
    def __init__(self,remetente,destino):
        self.envio = remetente
        self.remete = destino
        self.conteudo = []
        self.data_envio = hoje.date()
        self.hora = str(hoje.hour)+"h"+":"+str(hoje.minute)+"m"+":"+str(hoje.second)+"s\n"

msg = Mensagem("Diego","Jesus")


class Sistema:
    def __init__(self):
        self.cadastrados = {}
        self.conexao = psycopg2.connect(host="localhost", database="a_tarion", user="postgres", password="123")


    def __str__(self):
        return str(self.cadastrados)

    def Cadastrar_Usuario(self,nome,idade,profissao):
        if idade<=15:
            raise IdadeMenorException('Caracteres de idade inválidos')
        if len(nome)>=30:
            raise  NomeMaiorexception('Nome muito grande, tente denovo !')
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

        conta_existe = self.verifica_existe(email)
        if conta_existe:
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

    def get_cadastrados(self):
        print("CADASTRADOS:\n")
        cursor = self.conexao.cursor()
        cursor.execute('SELECT nome FROM usuario')
        while True:
            tupla = cursor.fetchone() # extrai elemento

            if not tupla:
                break
            print(tupla[0])
        cursor.close()
        self.conexao.commit()
            #return (self.cadastrados)

    def remover_conta(self):
        c_d=conta.logado
        t = input("Tens a certeza?[S/n]")
        if t=='s':
            cursor=self.conexao.cursor()
            cursor.execute('DELETE FROM cadastrados WHERE email =(%s)', (c_d))
            cursor.execute('DELETE FROM conta WHERE email =(%s)',(c_d))
            cursor.close()
            self.conexao.commit()

            '''if c_d in conta.logado:
                    if c_d in self.cadastrados.keys():
                        self.cadastrados.pop(c_d)
                    #conta.login= False # alteração feita
                        print("Conta removida, para acessar, crie outra conta" + "\n")
                    else:
                        print("conta não encontrada !!"+"\n")
            else:
                print("\nVocê deve entrar primeiro!\n")
        else:
            print("ufa, essa foi por pouco, em!")'''

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
            cursor.execute('UPDATE conta SET senha=(%s) WHERE senha=(%s)',(senha_nova,senha_antig))
            cursor.close()
            self.conexao.commit()
            self.cadastrados[email] = senha_nova
            print("Pronto, agora sua conta estará mais segura!"+"\n")
            print(self.cadastrados)
        else:
            print("dados inválidos!")

    def verifica_existe(self,email):
        '''existe = usr.logar(email,senha)
        if existe:
            print("Bem vindo de volta !")
        else:
            print("CAIU NO ELSE")'''
        if email in self.cadastrados.keys():
            return conta

    def main_conta(self):
        while True:


            print('\tr - Remover conta')
            print('\ti - atualizar Informacao')
            #print("\ts - atualizar Senha")
            print('\to - Sair(o)')
            opcao = input("sua escolha:")
            if opcao == 'r':
                self.remover_conta()
                self.Remover_Usuario()
                print(self.get_cadastrados())
                break
            if opcao=='i':
                print("\t\ts - trocar Senha")
                print("\t\tn - trocar Nome")
                print("\t\ti - mudar Idade")
                info = input("Tu desejas?")
                if info=='s':
                    email = input("informe o seu email:")
                    if email in conta.logado:
                        sistema.set_senha(email)
                    else:
                        print("\nvoce deve entrar com esta conta!\n")
                if info=='n':
                    novo_nome = input("Como você quer ser chamado?")
                    usr.set_nome(novo_nome)
                    print("VOCÊ AGORA É CONHECIDO COMO ",usr.nome)

                if info=='i':
                    nova_idade = int(input("nova idade:"))
                    usr.set_idade(nova_idade)

            if opcao=='o':
                conta.login = False
                conta.logado.remove(conta.email)
                print("usuario "+ conta.email+" saiu !")
                break

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
                    print(self.get_cadastrados())
                    usr.Logar()
                    self.main_conta()

                except IdadeMenorException as m:
                    print("Erro:",m)
                except ContaExistenteException as c:
                    print("Erro:",c)
                except NomeMaiorexception as nm:
                    print("ERRO:",nm)

            if esc=="e":

                email = input("Precisamos do seu email para acessar os serviços:\n")
                senha = input("Por favor, informe sua senha:\n")  ##colocar variáveis no sistema
                usr.logar(email,senha)
                self.verifica_existe(email)
                self.main_conta()

            if esc=="s":
                print("\n>>> OBRIGADO POR UTILIZAR O A_TARION! <<<\n")
                break


sistema = Sistema()
sistema.menu()
