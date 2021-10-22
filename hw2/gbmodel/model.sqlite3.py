"""
Data is stored in a SQLite database that looks something like the following:

+------------+------------------+------------+----------------+--------------+----------+
| Department | Course Number    | Quarter    | Year           | Instructor   | Review   |
+============+==================+============+----------------+--------------+----------+
| CS         | CS430            | Fall       | 2021           | Wu-Chang     | Great!   |
+------------+------------------+------------+----------------+--------------+----------+

This is created with the following SQL:

    create table coursereviews (department text, coursenumber integer, quarter text, year integer, instructor text, review text);

"""
from datetime import date
from .Model import Model
import sqlite3
DB_FILE = 'entries.db'    # file for our Database

class model(Model):
    def __init__(self):

        # Make sure our database exists
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("select count(rowid) from coursereviews")
        except sqlite3.OperationalError:
            cursor.execute("create table coursereviews (department text, coursenumber integer, quarter text, year integer, instructor text, review text)")
        cursor.close()

    def select(self):
        """
        Gets all rows from the database
        Each row contains: department, coursenumber, quarter, year, instructor, review
        :return: List of lists containing all rows of database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM coursereviews")
        return cursor.fetchall()

    def insert(self, department, coursenumber, quarter, year, instructor, review):
        """
        Inserts entry into database
        :param department: String
        :param coursenumber: Integer
        :param quarter: String
        :param year: Integer
        :param instructor: String
        :param review: String
        :return: True
        :raises: Database errors on connection and insertion
        """
        params = {'department':department, 'coursenumber':coursenumber, 'quarter':quarter, 'year':year, 'instructor':instructor, 'review':review }
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into coursereview (department, coursenumber, quarter, year, instructor, review) VALUES (:department, :coursenumber, :quarter, :year, :instructor, :review)", params)

        connection.commit()
        cursor.close()
        return True
