
print("Bem vindo a nossa escola!\n"
      "Você tem algumas opções:\n")

saida = input("0- Sair\n1- Aluno\n2- Professor\nEntre com os valores: ")

while saida != "0":
      if saida == "1":
            print("A aba de aluno tem essas opções:")
            aluno = input("0- Sair\n1- Adicionar aluno\n2- Verificar aluno\n3- Apagar aluno\n4- Atualizar aluno\nEntre com os valores:")
            if aluno == "1":
                  print("Adicionar aluno")
            elif aluno == "2":
                  print("Verificar aluno")
            elif aluno == "3":
                  print("Apagar aluno")
            elif aluno == "4":
                  print("Atualizar aluno")
            else:
                  print("Numero não existente!\n")
      elif saida == "2":
            print("A aba de professor tem essas opções:")
            professor = input(
                  "0- Sair\n1- Adicionar professor\n2- Verificar professor\n3- Apagar professor\n4- Atualizar professor\nEntre com os valores: ")
            if professor == "1":
                  print("Adicionar professor")
            elif professor == "2":
                  print("Verificar professor")
            elif professor == "3":
                  print("Apagar professor")
            elif professor == "4":
                  print("Atualizar professor")
            else:
                  print("Numero não existente!\n")
      else:
            print("Numero não existente!")
      saida = input("0- Sair\n1- Aluno\n2- Professor\nEntre com os valores: ")
