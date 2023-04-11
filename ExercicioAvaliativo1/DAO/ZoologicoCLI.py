from DAO.ZoologicoDAO import ZoologicoDAO
from model.Habitat import Habitat
from model.Cuidador import Cuidador
from model.Animal import Animal

class ZoologioCLI:

    def __init__(self):
        pass

    def menu(self):
        op = input("Escreva a opção que deseja: [1]Criar\n [2]Pesquisar\n [3]Atualizar\n [4]Deletar:")
        if op == 1:
            print("O animal foi criado com o id: ", ZoologioCLI.createAnimal(self))
        elif op == 2:
            ZoologioCLI.readAnimal(self)
        elif op == 3:
            ZoologioCLI.updateAnimal(self)
        elif op == 4:
            ZoologioCLI.deleteAnimal(self)


    def createAnimal(self):

        #inserindo os dados do cuidador
        idCuidador = input("Id do cuidador: ")
        nomeCuidador = input("Nome do cuidador: ")
        documentoCuidador = input("Documento do cuidador: ")
        cuidador = Cuidador(idCuidador, nomeCuidador, documentoCuidador)

        #inserindo os dados do habitat
        idHabitat = input("Id do habitat: ")
        nomeHabitat = input("Nome do habitat: ")
        tipoAmbienteHabitat = input("Tipo do ambiente do habitat: ")
        habitat = Habitat(idHabitat, nomeHabitat, tipoAmbienteHabitat, cuidador)

        #inserindo os dados do animal
        idAnimal = input("Id do animal: ")
        nomeAnimal = input("Nome do animal: ")
        especieAnimal = input("Especie do animal: ")
        idadeAnimal = input("Idade do animal: ")
        animal = Animal(idAnimal, nomeAnimal, especieAnimal, idadeAnimal, habitat)

        idAnimalCriado = ZoologicoDAO.create_animal(animal)
        return idAnimalCriado

    def readAnimal(self):
        id = input("Qual o id do animal a ser buscado?")
        ZoologicoDAO.read_animal_by_id(id)

    def updateAnimal(self):
        id = input("Qual o id do animal a ser atualizado?")
        print("Agora digite as informações a serem atualizadas")
        # inserindo os dados do cuidador
        idCuidador = input("Id do cuidador: ")
        nomeCuidador = input("Nome do cuidador: ")
        documentoCuidador = input("Documento do cuidador: ")
        cuidador = Cuidador(idCuidador, nomeCuidador, documentoCuidador)

        # inserindo os dados do habitat
        idHabitat = input("Id do habitat: ")
        nomeHabitat = input("Nome do habitat: ")
        tipoAmbienteHabitat = input("Tipo do ambiente do habitat: ")
        habitat = Habitat(idHabitat, nomeHabitat, tipoAmbienteHabitat, cuidador)

        # inserindo os dados do animal
        idAnimal = input("Id do animal: ")
        nomeAnimal = input("Nome do animal: ")
        especieAnimal = input("Especie do animal: ")
        idadeAnimal = input("Idade do animal: ")
        animal = Animal(idAnimal, nomeAnimal, especieAnimal, idadeAnimal, habitat)

        ZoologicoDAO.update_animal(id, animal)

    def deleteAnimal(self):
        id = input("Qual o id do animal a ser deletado?")
        ZoologicoDAO.delete_animal(id)
