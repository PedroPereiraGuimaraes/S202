class TeacherDatabase:
    def __init__(self, database):
        self.db = database

    def create(self, name, ano_nasc, cpf):
        query = f"CREATE (t:Teacher {{name: '{name}', ano_nasc: {ano_nasc}, cpf: '{cpf}'}})"
        self.db.execute_query(query)

    def insertClass(self, name, classes):
        query = f"MATCH (a:Teacher {{name:'{name}'}}),(c:Class {{class:'{classes}'}}) CREATE (a)-[:MINISTRA]->(c)"
        self.db.execute_query(query)

    def read(self, name):
        query = f"MATCH (t:Teacher {{name: '{name}'}}) RETURN t.name AS name, t.ano_nasc AS ano_nasc, t.cpf AS cpf"
        results = self.db.execute_query(query)
        return[(result["name"], result["ano_nasc"], result["cpf"]) for result in results]

    def delete(self, name):
        query = f"MATCH (t:Teacher {{name: '{name}'}}) DETACH DELETE t"
        self.db.execute_query(query)

    def update(self, name, parametro,  newparametro):
        query = f"MATCH (t:Teacher {{name: '{name}'}}) SET t.{parametro} = '{newparametro}'"
        self.db.execute_query(query)

    def exists(self, professor):
        query = f"MATCH (a:Teacher {{name:'{professor}'}}) RETURN a"
        result = self.db.execute_query(query)
        return len(result) > 0

    def read_all_teacher(self):
        query = "MATCH (t:Teacher) RETURN t.name  AS  name  ORDER BY  t.name"

        results = self.db.execute_query(query)

        return [result["name"] for result in results]