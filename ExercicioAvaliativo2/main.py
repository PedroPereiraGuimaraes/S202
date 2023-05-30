from database import Database
from teacher import TeacherDatabase
# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://44.211.89.106:7687", "neo4j", "ground-father-sound")
db.drop_all()

teacher_db = TeacherDatabase(db)

teacher_db.create("Chris Lima", 1956, "189.052.396-66")
print(teacher_db.read("Chris Lima"))
teacher_db.update("Chris Lima", "162.052.777-77")

# Fechando a conexão
db.close()