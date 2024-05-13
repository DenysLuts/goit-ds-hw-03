from pymongo import MongoClient

#%%
client = MongoClient('mongodb+srv://denluts33:PisiaSlona@denysluts.nr7rna0.mongodb.net/')
db = client['cats_database']
cats_collection = db['cats']
example_cat = {
    "name": "barsik",
    "age": 3,
    "features": ["ходить в капці", "дає себе гладити", "рудий"]
}
cats_collection.insert_one(example_cat)