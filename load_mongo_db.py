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

    # print message so user know so far so good    
    print("\nAttempting to load data...")
   
    # run scrape py, get new data from web content and load into mongo db
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
    # notify user that the process is completed    
    print("\n> Process Complete!\n")  
