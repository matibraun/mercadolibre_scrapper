import sqlite3

def create_database():

    try:
        import sqlite3

        ml_scrapper = sqlite3.connect('ml_scrapper.db')
        cursor = ml_scrapper.cursor()
        cursor.execute("CREATE TABLE ESCOBAR (index_ INTEGER, geographic_area TEXT, price_symbol VARCHAR (10), price INTEGER, surface_description TEXT, surface_symbol VARCHAR (10), surface_total INTEGER, surface_from INTEGER, surface_to INTEGER, link TEXT)")
        ml_scrapper.commit()
        ml_scrapper.close()

        print ('Database created successfully\n')

    except sqlite3.OperationalError:
        pass