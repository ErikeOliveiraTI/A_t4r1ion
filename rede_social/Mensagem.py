
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

'''
print("remetente:",msg.remete)
print("\tHora:"+msg.hora)
print("\tDia:",msg.data_envio)
'''