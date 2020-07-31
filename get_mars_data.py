import pymongo

# Create connection variable
mongo_conn = 'mongodb://localhost:27017'

def get_data():
    # Pass connection to the pymongo instance.
    client = pymongo.MongoClient(mongo_conn)
    
    # Connect to a database. Will create one if not already available.
    db = client.mars_db
    return db.mars_table.find_one()
    
# retrieve process name and post a wait message 
print(f">> Process name :{__name__}\nRetrieving Data. Please wait ... ")

if __name__ == "__main__":
    print("\nStill Working... Almost Done ...\n")
    mars_data = get_data()
    for record in mars_data:
        print(record)
    print("\nProcess Complete!\n") 
