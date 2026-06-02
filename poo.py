### Sem POO - Programação orientada a objeto
# cor = "Preto"
# modelo = "Civic"

# def acelear():
#     print("Acelerando o carro")

# print(cor)
# print(modelo)
# acelear()

### Com POO - Programação orientada a objeto

# class Carro:
#     def __init__(self, cor, modelo):
#         self.cor = cor
#         self.modelo = modelo

#     def acelerar(self):
#         print("Acelerando o carro")
        

# carro1 = Carro("Preto", "Civic")      
# carro2 = Carro("Vermelho", "Gol")

# print(carro1.cor)
# print(carro1.modelo)
# print(carro2.cor)
# print(carro2.modelo)
# carro1.acelerar()


# ### Atividade — POO em Python

# class Conta:
#     def __init__(self, titular, saldo):
#         self.titular = titular
#         self.saldo = saldo
#     def depositar(self, valor):
#         self.saldo += valor
#         print(f"Depósito de R${valor} realizado com sucesso. Saldo atual: R${self.saldo}")
#     def sacar(self, valor):
#         if valor <= self.saldo:
#             self.saldo -= valor
#             print(f"Saque de R${valor} realizado com sucesso. Saldo atual: R${self.saldo}")

#     def mostrar_saldo(self):
#         print(f"Saldo atual: R${self.saldo}")
        
# conta1 = Conta("João", 1000)
# conta1.depositar(500)
# print(conta1.saldo)  # Saída: 1500
# conta1.sacar(200)
# print(conta1.saldo)  # Saída: 1300
# conta1.sacar(1500)  # Saída: Saldo insuficiente

# ### Atividade 02 — POO em Python

# class Produto:
#     def __init__(self, nome, preco):
#         self.preco = preco

# produto1 = Produto("Notebook", 2500)
# produto1.exibir_informacoes()


### Atividade 03 – POO em Python

class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        media = (self.nota1 + self.nota2) / 2
        return media

    def verificar_situacao(self):
        media = self.calcular_media()
        if media >= 7:
            return "Aprovado"
        else:
            return "Reprovado"

# Instanciando o objeto e testando
aluno1 = Aluno("Maria", 8, 6)
print(f"Aluno: {aluno1.nome}")