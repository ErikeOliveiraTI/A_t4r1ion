from usuario import Usuario
from grupo import Grupo


class Administrador(Usuario):
    def __init__(self,codigo):
        Usuario.__init__(self,remetente=None,destino=None)
        self.codigo = codigo

    def criar_grupo(self):
        grupo = Grupo(nome=None,categoria=None,admin=None)
        global grupo

    def add_membro(self,convidado):
        grupo.membros.append(convidado)




