import pymongo

# Create connection variable
mongo_conn = 'mongodb://localhost:27017'

def get_data():
    # Pass connection to the pymongo instance.
    client = pymongo.MongoClient(mongo_conn)
    # Connect to a database. Will create one if not already available.
    db = client.mars_db
    return list(db.mars_db.find())
    
# This line is for training purposes only, you would not normally put this in code.
print(f"\nHey There, I'm the get data code.  My name is {__name__}")

if __name__ == "__main__":
    print("\nTesting Data Retrieval:....\n")
    mars_data = get_data()
    for record in mars_data:
        print(record)
    print("\nProcess Complete!\n")    