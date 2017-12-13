from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL']='sqlite:////tmp/test.b.d'
bd = SQLAlchemy(app)

#______________________________________________________________________

class Conta(bd.Model):
    #mapeando pro tipo banco de dados

    email = bd.Column(bd.String(25),primary_key=True)
    senha = bd.Column(bd.String(20),nullable=False)

    def __init__(self,email,senha, **kwargs):
        #chama o construtor do flask p/funcionar
        super(Conta,self).__init__(**kwargs)

        self.email  = email
        self.senha = senha
        self.amigos = []

    def add_friend(self):
        amg= input("procurar nick:")
        if amg==usr.nome:
            self.amigos.append(usr)
            print(self.amigos)


class Usuario:
    nome = bd.Column(bd.String(50),primary_key=True,nullable=False)
    idade = bd.Column(bd.Integer,nullable=False)

    def __init__(self,nome,idade,**kwargs):
        super(Usuario,self).__init__(**kwargs)
        self.nome = nome
        self.idade =idade

    def __str__(self):
        return str(self.nome)+"\n"+str(self.idade)


    def criar_conta(self):
        global conta
        email = input('SEU EMAIL:')
        senha = input("escolha uma senha:")
        conta = Conta(email, senha)

    def logar(self, email, senha):
        if email in sistema.cadastrados.keys():
            if senha in sistema.cadastrados.values():
                print("Usuário entrou !")
            else:
                print("senha incorreta")
        else:
            print("Usuário não registrado")

    def set_idade(self):
        nova_idade = int(input("nova idade:"))
        if nova_idade>0:
                self.idade= nova_idade
                print("idade atualizada:",self.idade)

class Sistema:
    def __init__(self):
        self.cadastrados = {}

    def __str__(self):
        return str(self.cadastrados)

    def cadastrar_conta(self, conta):
        self.cadastrados[conta.email] = conta.senha
        print("Usuário adicionado ao sistema com sucesso! "+"\n")

    def get_cadastrados(self):
        return (self.cadastrados)

    def remover_conta(self):
        c_d = input("conta a remover:")
        if c_d in self.cadastrados.keys():
            self.cadastrados.pop(c_d)
            print("Conta removida, para acessar, crie outra conta" + "\n")
        else:
            print("conta não encontrada !!"+"\n")

    def set_senha(self, email):
        senha_antig = input("informe a senha atual:")
        if senha_antig == self.cadastrados[email]:
            senha_nova = input("informe a senha nova:")
            self.cadastrados[email] = senha_nova
            print("Pronto, agora sua conta estará mais segura!"+"\n")
            print(self.get_cadastrados())
        else:
            print("dados inválidos!!!")

    def mostrar_contas(self):
        for c in conta.query.all():
            print(c.email)
    def pesquisar(self):
        amigo = conta.query.filter_by(email='joao').first()
        print(amigo.email)
    def consulta(self):
        resultado = bd.engine.execute("select * from Conta")
        for r in resultado:

            print(r)

    def menu(self):
        while True:
            print('1 - Criar conta')
            print('2 - Remover conta')
            print('3 - Atualizar idade')
            print('4 - Atualizar senha')
            print('5 - Consultar dados do Usuário')
            print('0 - Sair')

            opcao = int(input('Digite a opção:'))
            if opcao==0:
                bd.session.commit()
                print("ATÉ MAIS!")
                break
            if opcao==1:
                nome = input("informe seu nome:")
                idade = int(input("sua idade:"))
                usr = Usuario(nome, idade)
                global usr
                usr.criar_conta()
                self.cadastrar_conta(conta)
                bd.session.add(conta)
                self.mostrar_contas()

            if opcao==2:
                self.remover_conta()
                print(self.get_cadastrados())

            if opcao==3:
                usr.set_idade()
            if opcao==4:
                email=input("informe o seu email atual:")
                sistema.set_senha(email)
            if opcao==5:
                self.consulta()
            bd.session.commit()
            return opcao

#criando o banco de dados
bd.create_all()

sistema = Sistema()


#sistema.menu()
#sistema = Sistema()
'''usr = Usuario(nome, idade)
usr.criar_conta()
sistema.cadastrar_conta(conta)
'''
#print(sistema.get_cadastrados())
#sistema.remover_conta()
#print(sistema.get_cadastrados())