import csv
import psycopg2

def create_table(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS Professors (
                        id SERIAL PRIMARY KEY,
                        department TEXT,
                        name TEXT,
                        rvce_url TEXT,
                        google_scholar TEXT,
                        h_index INTEGER,
                        total_citations INTEGER,
                        max_citations INTEGER,
                        papers INTEGER
                    )''')

def insert_data(cursor, row):
    cursor.execute('''INSERT INTO Professors (department, name, rvce_url, google_scholar, h_index, total_citations, max_citations, papers)
                      VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''', row)

conn = psycopg2.connect(database="postgres", user="postgres", password="your_password", host="localhost", port="5432")
cursor = conn.cursor()

create_table(cursor)

with open('professor_scores.csv', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader) 
    for row in csvreader:
        row = row[:-1]
        insert_data(cursor, row)

conn.commit()
conn.close()

print("Data has been successfully inserted into the database.")
