import sqlite3

class Person:

    def __init__(self, id=0, first_name="", last_name="", age=0):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.connection = sqlite3.connect("mydata.db")
        self.cursor = connection.cursor()

    def load_person(self, id):
        self.cursor.execute("""
        SELECT * FROM PEOPLE
        WHERE ID = {}
        """).format(id)

        results = self.cursor.fetchone()
        self.id_number = id_number
        self.first_name = results[1]
        self.last_name = results[2]
        self.age = results[3]

connection = sqlite3.connect("mydata.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS PEOPLE (
    ID INTEGER PRIMARY KEY, 
    first_name VARCHAR(32),
    last_name VARCHAR(32),
    age INTEGER
)
""")

cursor.execute("""
INSERT INTO PEOPLE VALUES
(1, 'Paul', 'Smith', 24),
(2, 'Mark', 'Johnson', 22),
(3, 'Anna', 'Smith', 32)
""")

cursor.execute("""
SELECT * FROM PEOPLE
WHERE last_name = 'Smith'
""")

rows = cursor.fetchall()
print(rows)

connection.commit()
connection.close()

p1 = Person()
p1.load_person(1)
print(p1.id)
print(p1.first)
print(p1.list)
print(p1.age)


