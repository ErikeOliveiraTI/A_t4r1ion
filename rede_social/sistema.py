# -*- coding: utf-8 -*-

import psycopg2
from usuario import Usuario

class Sistema:
    def __init__(self):
        self.conexao = psycopg2.connect(host="localhost", database="A_tarion", user="postgres", password="postgres")
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
            print("0 - Entrar")
            print("1 - Registrar-se")
            

            print('1 - Criar conta')
            print('2 - Remover conta')
            print('3 - Atualizar idade')
            print('4 - Atualizar senha')
            print('0 - Sair')

            opcao = int(input('Digite a opção:'))
            if opcao==0:
                print("")
                print("TE VEJO MAIS TARDE!")
                break
            if opcao==1:
                nome = input("informe seu nome:")
                idade = int(input("sua idade:"))
                usr = Usuario(nome, idade)
                usr.criar_conta()
                self.cadastrar_conta(conta)
                print(self.get_cadastrados())

            if opcao==2:
                self.remover_conta()
                print(self.get_cadastrados())

            if opcao==3:
                usr.set_idade()
            if opcao==4:
                email= input("informe o seu email atual:")
                sistema.set_senha(email)
sistema = Sistema()
sistema.menu()