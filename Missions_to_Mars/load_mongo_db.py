# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo
from scrape_mars import scrape

# Create connection variable
conn = 'mongodb://localhost:27017'



# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.mars_db

# Drops collection if available to remove duplicates
db.mars_table.drop()

    

# def load_data():
print("\nAttempting to load data...")
# Creates a collection in the database and inserts two documents

mars_table = scrape()
db.mars_table.update_one({}, {"$set": mars_table}, upsert=True)
    


if __name__ == "__main__":
    print("\nRetrieving Data ...")
    print("\nPlease wait ...")
    mars_Query = list(db.mars_table.find())
    print("\nMars data :: \n")
    for record in mars_Query:
        print(record)
    print("\nProcess Complete!\n")  