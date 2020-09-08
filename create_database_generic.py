import sqlite3

def create_database(database_name):

    try:
        import sqlite3
        database_name_with_extention = database_name.replace(' ', '_') + ".db"
        ml_scrapper = sqlite3.connect(database_name_with_extention)
        cursor = ml_scrapper.cursor()
        cursor.execute("CREATE TABLE SCRAPPED_INFO (index_ INTEGER PRIMARY KEY NOT NULL, description TEXT, original_price_symbol VARCHAR (10), original_price INTEGER, discounted_price_symbol VARCHAR (10), discounted_price INTEGER, discount_percentage TEXT, type_of_delivery TEXT, date_of_arrival TEXT, installments TEXT, link TEXT)")
        ml_scrapper.commit()
        ml_scrapper.close()

        print ('Database created successfully.\n')

    except sqlite3.OperationalError:
        pass
