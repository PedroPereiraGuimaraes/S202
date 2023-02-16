class Animal:
    def __int__(self, nome, idade, especie, cor, som):
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.cor = cor
        self.som = som

    def emitir_som(self):
        print(self.som)

    def muda_cor(self, nova_cor):
        self.cor = nova_cor


class Elefante(Animal):
    def __init__(self, nome, idade, especie, cor, som, tamanho):
        super().__init__(nome, idade, especie, cor, som)
        self.tamanho = tamanho

    def trombar(self):
        print(self.som)

    def mudar_tamanho(self, novo_tamanho):
        self.tamanho = novo_tamanho


nome = input("Digite o nome do seu elefante:")
idade = int(input("Digite a idade do seu elefante:"))
especie = input("Digite a especie do seu elefante:")
cor = input("Digite a cor do seu elefante:")
tamanho = input("Digite o tamanho do seu elefante:")

if especie == "Africano" and idade < 10:
    tamanho = "pequeno"
    som = "Paaah"
elif especie == "Africano" and idade >= 10:
    tamanho = "grande"
    som = "PAHHHHHH"
else:
    som = "FOONN"

elefante = Elefante(nome, idade, especie, cor, som, tamanho)

elefante.trombar()
print(elefante.tamanho)
