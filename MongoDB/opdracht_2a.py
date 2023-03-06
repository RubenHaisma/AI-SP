import pymongo

# Maak verbinding met de MongoDB-server
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Selecteer de database
db = client["local"]

# Selecteer de collectie
collection = db["products"]

# Wat is de naam en prijs van het eerste product in de database?
first_product = collection.find_one()
print("Naam van het eerste product:", first_product["name"])
print("Prijs van het eerste product:", first_product["price"])

# Geef de naam van het eerste product waarvan de naam begint met een 'R'?
r_product = collection.find_one({"name": {"$regex": "^R"}})
print("Naam van het eerste product dat begint met een 'R':", r_product["name"])

# Wat is de gemiddelde prijs van de producten in de database?
average_price = collection.aggregate([
    {"$group": {"_id": None, "avg_price": {"$avg": "$price.selling_price"}}}
])

# Print het gemiddelde van de prijzen
print("Gemiddelde prijs van de producten:", list(average_price)[0]["avg_price"])



