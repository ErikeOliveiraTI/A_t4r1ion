from datetime import *
class Mensagem:
    def __init__(self,escrito, email_r, email_d):
        self.escrito=escrito
        self.email_remetente=email_r
        self.email_destino=email_d
        self.data=datetime.today()

