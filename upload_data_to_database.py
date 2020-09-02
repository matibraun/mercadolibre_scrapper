import sqlite3



ingreso = [(indx_clean[index], zonas_clean[index], price_symbols_clean[index], prices_clean[index], areas_clean[index],
            links_clean[index])]
ml_scrapper = sqlite3.connect('ml_scrapper.db')
cursor = ml_scrapper.cursor()
cursor.executemany("INSERT INTO ESCOBAR VALUES (?, ?, ?, ?, ?, ?)", ingreso)
ml_scrapper.commit()
ml_scrapper.close()