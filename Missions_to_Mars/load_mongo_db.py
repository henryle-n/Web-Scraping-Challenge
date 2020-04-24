# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.mars_db

# Drops collection if available to remove duplicates
db.mars_db.drop()

print("\nAttempting to load data...")
# Creates a collection in the database and inserts two documents

mars_data = scrape.scrape()
db.mars_db.update({}, mars_data, upsert=True)
    


if __name__ == "__main__":
    print("\nAttempting to retrieve any loaded data....")
    mars_info = list(db.mars_db.find())
    print("\nMars data :: \n")
    for record in mars_info:
        print(record)
    print("\nProcess Complete!\n")  