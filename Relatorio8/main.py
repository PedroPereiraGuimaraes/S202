from database import Database
from game import GameDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://34.201.7.64:7687", "neo4j", "appearances-arithmetic-interface")
db.drop_all()

game_db = GameDatabase(db)

#CRIANDO UM PLAYER
game_db.create_player("Pedro", 1666)
game_db.create_player("Joaquim", 1987)
game_db.create_player("Marina", 2005)

#CRIANDO UM JOGO
game_db.create_match("Pedro", 1666, "Joaquim", 1987, 1, 300)
game_db.create_match("Pedro", 1666,"Marina", 2005, 1, 200)

#VENDO O PLAYER E O JOGO
print(game_db.get_player())
print(game_db.get_match())


#ATUALIZANDO O PLAYER
game_db.update_player("Pedro", "Marcos", 1666)
print(game_db.get_player())

#DELETANDO O PLAYER
game_db.delete_player("Marcos", 1666)
print(game_db.get_player())

# Fechando a conexão
db.close()