import csv
import sqlite3

def insert_data(cursor, row):
    cursor.execute('''INSERT INTO Professors (department, name, google_scholar, h_index, total_citations, max_citations, papers)
                      VALUES (?, ?, ?, ?, ?, ?, ?)''', row)

conn = sqlite3.connect('professors.db')
cursor = conn.cursor()

with open('professor_scores.csv', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader) 
    for row in csvreader:
        insert_data(cursor, row)

conn.commit()
conn.close()
