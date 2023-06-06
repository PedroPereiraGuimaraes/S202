class ClassDatabase:
    def __init__(self, database):
        self.db = database

    def create(self, name, creation):
        query = f"CREATE (t:Class {{class: '{name}', creation: '{creation}'}})"
        self.db.execute_query(query)

    def read(self, name):
        query = f"MATCH (t:Class {{name: '{name}'}}) RETURN t.name AS name, t.creation AS creation"
        results = self.db.execute_query(query)
        return[(result["name"], result["creation"]) for result in results]

    def delete(self, name):
        query = f"MATCH (t:Class {{name: '{name}'}}) DELETE t"
        self.db.execute_query(query)

    def update(self, name, newparametro, parametro):
        query = f"MATCH (t:Class {{name: '{name}'}}) SET t.{newparametro} = '{parametro}'"
        self.db.execute_query(query)

    def get_all_students(self, class_name):
        query = f"MATCH (c:Class {{class: '{class_name}'}})<-[:FAZ_PARTE]-(a:Student) RETURN a.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def get_teacher(self, class_name):
        query = f"MATCH (c:Class {{class: '{class_name}'}})<-[:MINISTRA]-(t:Teacher) RETURN t.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def exists(self, name):
        query = f"MATCH (t:Class {{class: '{name}'}}) RETURN t"
        result = self.db.execute_query(query)
        return len(result) > 0

    def relation(self, name, classes):
        query = f"MATCH (a:Teacher {{name:'{name}'}}),(c:Class {{class:'{classes}'}}) RETURN EXISTS((a)-[:MINISTRA]->(c)) AS relationship_exists"
        result = self.db.execute_query(query)
        relationship_exists = result[0]["relationship_exists"]

        if not relationship_exists:
            return False
        else:
            return True
