class StudentDatabase:
    def __init__(self, database):
        self.db = database

    def create(self, name, ano_nasc, cpf):
        query = f"CREATE (t:Student {{name: '{name}', ano_nasc: {ano_nasc}, cpf: '{cpf}'}})"
        self.db.execute_query(query)

    def read(self, name):
        query = f"MATCH (t:Student {{name: '{name}'}}) RETURN t.name AS name, t.ano_nasc AS ano_nasc, t.cpf AS cpf"
        results = self.db.execute_query(query)
        return[(result["name"], result["ano_nasc"], result["cpf"]) for result in results]

    def delete(self, name):
        query = f"MATCH (t:Student {{name: '{name}'}}) DELETE t"
        self.db.execute_query(query)

    def update(self, name, newCpf):
        query = f"MATCH (t:Student {{name: '{name}'}}) SET t.cpf = '{newCpf}'"
        self.db.execute_query(query)
