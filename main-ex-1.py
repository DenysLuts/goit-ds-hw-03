
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb+srv://denluts33:PisiaSlona@denysluts.nr7rna0.mongodb.net/')  # Підключення до локального MongoDB
db = client['cats_database']
cats_collection = db['cats']

# Читання (Read)

def read_all_cats():
    """Функція для виведення всіх записів із колекції."""
    for cat in cats_collection.find():
        print(cat)

def read_cat_by_name(name):
    """Функція для виведення інформації про кота за ім'ям."""
    cat = cats_collection.find_one({"name": name})
    if cat:
        print(cat)
    else:
        print("Кіт з таким ім'ям не знайдено.")

# Оновлення (Update)

def update_cat_age(name, new_age):
    """Функція для оновлення віку кота за ім'ям."""
    cats_collection.update_one({"name": name}, {"$set": {"age": new_age}})
    print("Вік кота оновлено.")

def add_feature_to_cat(name, new_feature):
    """Функція для додавання нової характеристики до списку features кота за ім'ям."""
    cats_collection.update_one({"name": name}, {"$push": {"features": new_feature}})
    print("Нову характеристику додано до кота.")

# Видалення (Delete)

def delete_cat_by_name(name):
    """Функція для видалення запису з колекції за ім'ям тварини."""
    cats_collection.delete_one({"name": name})
    print("Кіт видалений.")

def delete_all_cats():
    """Функція для видалення всіх записів із колекції."""
    cats_collection.delete_many({})
    print("Всі коти видалені.")

if __name__ == "__main__":
    # Приклад використання функцій
    read_all_cats()
    read_cat_by_name("barsik")
    update_cat_age("barsik", 4)
    add_feature_to_cat("barsik", "любить спати на сонці")
    delete_cat_by_name("barsik")
    delete_all_cats()
