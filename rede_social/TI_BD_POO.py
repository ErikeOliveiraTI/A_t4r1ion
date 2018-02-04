
'''
# Crie o banco de dados em sqlite e salva no arquivo: /tmp/test.db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
bd = SQLAlchemy(app)


class Conta(bd.Model):
    """Representa uma Conta bancária. Conta simplificada por questões didáticas."""

    # mapeia os atributos a tipos em banco de dados
    numero = bd.Column(db.String(5), primary_key=True)
    saldo = bd.Column(bd.Float, nullable=False, default=0)

    # necessário alterar o construtor e receber o **kwargs (o flask sqlalchemy precisa disso para funcionar)
    def __init__(self, numero='', saldo=0, **kwargs):
        # necessário chamar o superconstrutor para o flask sqlalchemy funcionar
        super(Conta, self).__init__(**kwargs)
        self.numero = numero
        self.saldo = saldo

    def creditar(self, valor):
        self.saldo += valor

    def debitar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor

    def transferir(self, valor, destino):
        self.debitar(valor)
        destino.creditar(valor)

    def get_saldo(self):
        return self.saldo

# cria o banco de dados
bd.create_all()

c = Conta(email,senha)

# acrescenta à sessão do banco de dados uma conta. Lembrando que não será salvo em banco enquanto não for dado o commit
bd.session.add(c)

# commita as alterações no banco de dados
bd.session.commit()

# percorre todas as contas do banco
for conta in Conta.query.all():
    print(conta.email)

# faz uma pesquisa em Conta, filtrando por número
c1 = Conta.query.filter_by(numero=1).first()
print(c1.numero)

# realiza uma consulta direta no banco, com o SQL que você passar
results = bd.engine.execute("select * from Conta")
for r in results:
    print(r)


'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Crie o banco de dados em sqlite e salva no arquivo: /tmp/test.db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
bd = SQLAlchemy(app)


#*________________________________________________________________________*
class Conta:
    email = bd.Column(bd.String(20),primary_key=True)
    senha = bd.Column(bd.String(50), nullable=False, default=123)

    def __init__(self,email,senha, **kwargs):
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
    def __init__(self,nome,idade):
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
            print(self.cadastrados)
        else:
            print("dados inválidos!")

    def menu(self):
        while True:

            print('1 - Criar conta')
            print('2 - Remover conta')
            print('3 - Atualizar idade')
            print('4 - Atualizar senha')
            print('5 - pesquisar contas')
            print('0- Sair')

            opcao = int(input('Digite a opção:'))
            if opcao==0:
                bd.session.commit()
                break
            if opcao==1:
                nome = input("informe seu nome:")
                idade = int(input("sua idade:"))
                usr = Usuario(nome, idade)
                usr.criar_conta()
                self.cadastrar_conta(conta)
                print(self.get_cadastrados())
                bd.session.add(conta) # adicionando a conta ao banco de dados
                bd.session.commit()

            if opcao==2:
                self.remover_conta()
                print(self.get_cadastrados())
                bd.session.commit()

            if opcao==3:
                usr.set_idade()
            if opcao==4:
                email= input("informe o seu email atual:")
                sistema.set_senha(email)
            if opcao==5:
                pesq = input("quem é:")
                cont= conta.query.filter_by(email=pesq)
                print(cont.email)


# cria o banco de dados
bd.create_all()
sistema = Sistema()
#sistema.menu()
bd.session(sistema.menu())
#sistema = Sistema()
'''usr = Usuario(nome, idade)
usr.criar_conta()
sistema.cadastrar_conta(conta)
'''
#print(sistema.get_cadastrados())
#sistema.remover_conta()
#print(sistema.get_cadastrados())

'''
# acrescenta à sessão do banco de dados uma conta. Lembrando que não será salvo em banco enquanto não for dado o commit

# commita as alterações no banco de dados
bd.session.commit()

# percorre todas as contas do banco
for conta in Conta.query.all():
    print(conta.email)

# faz uma pesquisa em Conta, filtrando por número
c1 = Conta.query.filter_by(numero=1).first()
print(c1.numero)

# realiza uma consulta direta no banco, com o SQL que você passar
results = bd.engine.execute("select * from Conta")
for r in results:
    print(r)
'''