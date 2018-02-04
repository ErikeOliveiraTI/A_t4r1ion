from conta import Conta
from sistema import sistema

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
        conta = Conta(email, senha,usr=None)
        global conta

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
    def Logar(self,c,s):
        c = input("Precisamos do seu email para acessar os serviços:\n")
        s = input("Por favor, informe sua senha:") ##colocar variáveis no sistema

