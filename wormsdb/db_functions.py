import os
import sqlite3 as lite
import time

con = None
database_location = os.path.join(os.path.dirname(__file__), 'database/WORMS.db')

# Opening the worms database
def open_db():
    try:
        con = lite.connect(database_location)
        return con
    except lite.Error:
        return None

# Close it after use
def close_db(con):
    con.close()

sample_sn_ids = ['urn:lsid:marinespecies.org:taxname:519212', 'urn:lsid:marinespecies.org:taxname:399249', 'urn:lsid:marinespecies.org:taxname:170605', '????????']
semple_sn = ['Polymastia littoralis', 'Scorpaena cocosensis', 'Neoscopelarchoides', 'Pippo Pippo']



def get_record(con, table, field_name, value, fields):
    """ Query the WORMS db and gets a single record from the database
        :param con : The database connection
        :param table - The table to interrogate
        :param field_name: The Column to interrogate
        :param value : The value sought
        :param fields : The table columns

        :returns a dictionary mapped to the fields or None if no record is found
        """

    record = None
    cur = con.execute(f"SELECT * from {table} where {field_name}='{value}'")
    retrieved_record = cur.fetchone()

    if retrieved_record is not None:
        record = dict(zip(fields, retrieved_record))

    return record




# con = open_db()
# verify_querying()
# close_db(con)
