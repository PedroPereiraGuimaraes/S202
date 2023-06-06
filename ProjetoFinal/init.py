from database import Database
from classes import  ClassDatabase
from teacher import TeacherDatabase
from student import StudentDatabase
# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://34.200.232.234:7687", "neo4j", "outfit-decisions-headquarters")

class DBCreate:

    nomes_materias = ["Matemática", "Física", "Química", "Biologia", "História", "Geografia", "Inglês", "Português",
                      "Artes", "Educação Física"]
    professores = [
        {"nome": "Pedro", "ano": 2001, "cpf": 123123123},
        {"nome": "Maria", "ano": 2002, "cpf": 456456456},
        {"nome": "João", "ano": 2003, "cpf": 789789789},
        {"nome": "Ana", "ano": 2004, "cpf": 987654321},
        {"nome": "Carlos", "ano": 2005, "cpf": 111222333},
        {"nome": "Juliana", "ano": 2006, "cpf": 444555666},
        {"nome": "Roberto", "ano": 2007, "cpf": 777888999},
        {"nome": "Sandra", "ano": 2008, "cpf": 333222111},
        {"nome": "Lucas", "ano": 2009, "cpf": 555444333},
        {"nome": "Isabela", "ano": 2010, "cpf": 222333444}
    ]
    turmas_professores = [
        {"professor": "Pedro", "turma": "Matemática"},
        {"professor": "Maria", "turma": "Física"},
        {"professor": "João", "turma": "Química"},
        {"professor": "Ana", "turma": "Biologia"},
        {"professor": "Carlos", "turma": "História"},
        {"professor": "Juliana", "turma": "Geografia"},
        {"professor": "Roberto", "turma": "Inglês"},
        {"professor": "Sandra", "turma": "Português"},
        {"professor": "Lucas", "turma": "Artes"},
        {"professor": "Isabela", "turma": "Educação Física"}
    ]

    def createDB(self):

        class_db = ClassDatabase(db)
        teacher_db = TeacherDatabase(db)

        for nome in DBCreate.nomes_materias:
            if not class_db.exists(nome):
                class_db.create(nome, "2015")

        for professor in DBCreate.professores:
            if not teacher_db.exists(professor["nome"]):
                teacher_db.create(professor["nome"], professor["ano"], professor["cpf"])


        for item in DBCreate.turmas_professores:
            if not class_db.relation(item["professor"], item["turma"]):
                teacher_db.insertClass(item["professor"], item["turma"])
