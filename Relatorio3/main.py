from database import Database
from save_json import writeAJson

##connectando ao Database
db = Database(database="dex", collection="pokemons")
db.resetDatabase()

#pokemons = db.collection.find()
#for pokemon in pokemons: #printando ela
#    print(pokemon)


#pegando por tipo poison e defesa maior que 80
pokemon = db.collection.find({"type": "Poison", "base.Defense": { "$gte": 80 }})
writeAJson(pokemon, "pokemon_poison")

#pegando por tipo fire e defesa menor que 60
pokemon = db.collection.find({"type": "Fire", "base.Defense": { "$lte": 60 }})
writeAJson(pokemon, "pokemon_fire")

#pegando por tipo flying e speed maior que 80
pokemon = db.collection.find({"type": "Flying", "base.Speed": { "$gte": 80 }})
writeAJson(pokemon, "pokemon_flying")

#pegando por tipo fire e flying
pokemon = db.collection.find({"type": ["Fire","Flying"]})
writeAJson(pokemon, "pokemon_flying_fire")

#pegando os com o nome com 5 ou menos letras
def get_5_letters_or_less(collection):
  names = collection.find({}, {"name": 1})
  four_letters_or_less = []
  for name in names:
    if len(name["name"].keys()) <= 5:
      if all(len(word) <= 5 for word in name["name"].values()):
        four_letters_or_less.append(name["name"].values())
  return four_letters_or_less

writeAJson(get_5_letters_or_less(db.collection), "pokemon_5_words_or_less")