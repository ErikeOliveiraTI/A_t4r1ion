#from usuario import Usuario

class Conta:
    def __init__(self,email,senha,usr=None):
        self.email  = email
        self.senha = senha
        self.amigos = []
        self.login()


    def add_friend(self):
        amg= input("procurar nick:")
        if amg==usr.nome:
            self.amigos.append(usr)
            print(self.amigos)
