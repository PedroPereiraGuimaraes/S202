class StudentDatabase:
    def __init__(self, database):
        self.db = database

    def create(self, name, ano_nasc, cpf):
        query = f"CREATE (t:Student {{name: '{name}', ano_nasc: {ano_nasc}, cpf: '{cpf}'}})"
        self.db.execute_query(query)

    def insertClass(self, name, classes):
        query = f"MATCH (a:Student {{name:'{name}'}}),(c:Class {{class:'{classes}'}}) CREATE (a)-[:FAZ_PARTE]->(c)"
        self.db.execute_query(query)

    def read(self, name):
        query = f"MATCH (t:Student {{name: '{name}'}}) RETURN t.name AS name, t.ano_nasc AS ano_nasc, t.cpf AS cpf"
        results = self.db.execute_query(query)
        return[(result["name"], result["ano_nasc"], result["cpf"]) for result in results]

    def delete(self, name):
        query = f"MATCH (t:Student {{name: '{name}'}}) DETACH DELETE t"
        self.db.execute_query(query)

    def update(self, name, parametro,  newparametro):
        query = f"MATCH (t:Student {{name: '{name}'}}) SET t.{parametro} = '{newparametro}'"
        self.db.execute_query(query)

    def read_all_student(self):
        query = "MATCH (s:Student) RETURN s.name  AS  name ORDER BY  s.name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]
