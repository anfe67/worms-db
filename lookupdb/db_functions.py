""" Simple wrapper to query the WORMS database in SQLite format """
import os
import sqlite3 as lite
import sys

# this is a pointer to the module object instance itself.
this = sys.modules[__name__]
this.conn = None
this.database_location = os.path.join(os.path.dirname(__file__), 'database/EUROBIS_QC_LOOKUP_DB.db')


# Opening the worms database
def open_db():
    try:
        this.conn = lite.connect(this.database_location)
        return this.conn
    except lite.Error:
        this.conn = None
        return None


# Close it after use
def close_db():
    this.conn.close()
    this.conn = None


def get_record(table, field_name, value, fields):
    """ Query the WORMS db and gets a single record from the database
        :param table - The table to interrogate
        :param field_name: The Column to interrogate
        :param value : The value sought
        :param fields : The table columns

        :returns a dictionary mapped to the fields or None if no record is found
        """

    record = None
    cur = this.conn.execute(f"SELECT * from {table} where {field_name}='{value}'")
    retrieved_record = cur.fetchone()

    if retrieved_record is not None:
        record = dict(zip(fields, retrieved_record))

    return record
