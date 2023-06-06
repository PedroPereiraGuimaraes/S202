from database import Database
from classes import  ClassDatabase
from teacher import TeacherDatabase
from student import StudentDatabase
from init import DBCreate
# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://34.200.232.234:7687", "neo4j", "outfit-decisions-headquarters")

class_db = ClassDatabase(db)
teacher_db = TeacherDatabase(db)
student_db = StudentDatabase(db)
create = DBCreate

create.createDB(db)

print("Bem vindo a nossa escola!\n"
      "Você tem algumas opções:\n")

saida = input("0- Sair\n1- Aluno\n2- Professor\n3- Verificar turmas\n4- Ver todos os professores\n5- Ver todos os alunos\nEntre com os valores: ")

while saida != "0":
      if saida == "1":
            print("A aba de aluno tem essas opções:")
            aluno = input("0- Sair\n1- Adicionar aluno\n2- Verificar aluno\n3- Apagar aluno\n4- Atualizar aluno\nEntre com os valores:")
            if aluno == "1":
                  name = input("Nome: ")
                  year = input("Ano de nascimento: ")
                  cpf = input("CPF: ")
                  student_db.create(name, year, cpf)
                  for nome in create.nomes_materias:
                      student_db.insertClass(name, nome)
            elif aluno == "2":
                  name = input("Digite o nome para a busca:")
                  print(student_db.read(name))
            elif aluno == "3":
                  name = input("Digite o nome do aluno a ser deletado:")
                  student_db.delete(name)
            elif aluno == "4":
                  name = input("Digite o aluno que quer modificar:")
                  parameter = input("Digite o parametro que quer modificar(nome,ano_nasc,cpf):")
                  value = input("Digite o valor do parametro:")
                  student_db.update(name,parameter,value)

      elif saida == "2":
            print("A aba de professor tem essas opções:")
            professor = input("0- Sair\n1- Adicionar professor\n2- Verificar professor\n3- Apagar professor\n4- Atualizar professor\nEntre com os valores:")
            if professor == "1":
                name = input("Nome: ")
                year = input("Ano de nascimento: ")
                cpf = input("CPF: ")
                teacher_db.create(name, year, cpf)
                turma = input("Insira a materia do professor:")
                teacher_db.insertClass(name, turma)
            elif professor == "2":
                name = input("Digite o nome para a busca:")
                print(teacher_db.read(name))
            elif professor == "3":
                name = input("Digite o nome do professor a ser deletado:")
                teacher_db.delete(name)
            elif professor == "4":
                name = input("Digite o professor que quer modificar:")
                parameter = input("Digite o parametro que quer modificar(nome,ano_nasc,cpf):")
                value = input("Digite o valor do parametro:")
                teacher_db.update(name, parameter, value)
      elif saida == "3":
          classes = input("Digite o nome da materia:")
          print("Professor", class_db.get_teacher(classes))
          print("Alunos", class_db.get_all_students(classes))
      elif saida == "4":
          print(teacher_db.read_all_teacher())
      elif saida == "5":
          print(student_db.read_all_student())
      else:
            print("Numero não existente!")
      saida = input("0- Sair\n1- Aluno\n2- Professor\n3- Verificar turmas\n4- Ver todos os professores\n5- Ver todos os alunos\nEntre com os valores: ")

