import pymongo

# Connect to MongoDB
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# Create the database
mydb = myclient["dskola"]

# Create the collection
mycol = mydb["books"]

print("Database and collection created successfully.")
