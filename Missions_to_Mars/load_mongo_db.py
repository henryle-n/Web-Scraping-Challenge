# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo
from scrape_mars import scrape

# Create connection variable
conn = 'mongodb://localhost:27017'


def load_new_data():
    
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
    return mars_table


if __name__ == "__main__":
    print("\n> Retrieving Data ...")
    print("\n> Please wait ...")
    mars_Query = load_new_data()
    print("\nMars data :: \n")
    for record in mars_Query:
        print(record)
    print("\n> Process Complete!\n")  