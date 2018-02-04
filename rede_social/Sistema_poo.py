from Usuario_poo import Usuario

class Sistema:
    def __init__(self):
        self.cadastrados = {}
        self.apelidos = []


    def __str__(self):
        return str(self.cadastrados)

    def cadastrar_usr(self):
        email= input("seu email:")
        idade= input("sua idade:")
        senha = input("escolha uma senha:")

        self.ver_usr()
        if email!=self.ver_usr():
            global conta
            conta = Usuario(email,senha,idade)
            self.cadastrados[email] = senha
        return("Usuário cadastrado !!")

    def ver_usr(self,email):  #ver se usuário já existe
        if email in self.cadastrados.keys():
            return email

sistema = Sistema()