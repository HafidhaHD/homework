import pymongo
from datetime import datetime
import math
import random
from bson.objectid import ObjectId

# Connect to MongoDB
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# Access the database
mydb = myclient["dskola"]

# Access the collection
mycol = mydb["books"]

# Helper function to get a valid day for a given month and year
def get_valid_day(year, month):
    if month == 2:
        # Handle February
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            # Leap year
            return random.randint(1, 29)
        else:
            # Non-leap year
            return random.randint(1, 28)
    elif month in [4, 6, 9, 11]:
        # April, June, September, November
        return random.randint(1, 30)
    else:
        # January, March, May, July, August, October, December
        return random.randint(1, 31)

# Insert data into the collection
for i in range(100):
    month = random.randint(1, 12)
    year = 2024
    day = get_valid_day(year, month)
    my_dict = {
        "title": "Book Title " + str(i),
        "author": "Author " + str((i % 10) + 1),  # 10 different authors
        "genre": random.choice(["Fiction", "Dystopian", "Adventure", "Science Fiction", "Fantasy"]),  # 5 different genres
        "published_year": 1950 + (i % 70),  # Published between 1950 and 2019
        "copies_available": math.floor(random.randint(1, 9) * 10) + 1,  # 1 to 10 copies available
        "borrowed_by": [
            {
                "user_id": ObjectId(),
                "borrowed_date": datetime(year, month, day),  # Valid borrowed date in 2024
                "return_date": None
            }
        ]
    }
    mycol.insert_one(my_dict)

print("Data inserted successfully.")
