from db import run_query_select, run_update_query
#question 2
run_update_query("""DROP TABLE IF EXISTS authors;""")
run_update_query("""DROP TABLE IF EXISTS books;""")


run_update_query("""CREATE TABLE authors (
  id      INTEGER PRIMARY KEY,
  name    TEXT    NOT NULL,
  country TEXT
);"""
)

run_update_query("""
CREATE TABLE books (
  id        INTEGER PRIMARY KEY,
  title     TEXT    NOT NULL,
  author_id INTEGER,
  year      INTEGER NOT NULL,
  FOREIGN KEY (author_id) REFERENCES authors(id)
);
""")

#question 3
run_update_query(f"INSERT INTO authors VALUES (?,?,?)",(1,'George Orwell','UK'))
run_update_query(f"INSERT INTO authors VALUES (?,?,?)",(2,'Gabriel García Márquez','Colombia'))
run_update_query(f"INSERT INTO authors VALUES (?,?,?)",(3,'Haruki Murakami','Japan'))
run_update_query(f'INSERT INTO books VALUES (?,?,?,?)',(1,'1984',1,1949))
run_update_query(f'INSERT INTO books VALUES(?,?,?,?)', (2,'Animal Farm',1, 1945))
run_update_query(f'INSERT INTO books VALUES(?,?,?,?)', (3,'One Hundred Years of Solitude', 2, 1967))
run_update_query(f'INSERT INTO books VALUES(?,?,?,?)',(4,'Norwegian Wood',3, 1987))

run_update_query('PRAGMA foreign_keys = ON;')

#question 4
books = run_query_select(f'SELECT * FROM books;')
for row in books:
    print({'title': row ['title']})
print (' ')
i = 0
while i < 42:
    i+=1
    print('-',end='')


#question 5
book = run_query_select(f'select * from books WHERE year > 1960;')
for row in book:
    print (' ')
    print({'title': row ['title']})
    print({'year': row ['year']})
print (' ')
i = 0
while i < 42:
    i+=1
    print('-',end='')
print (' ')

#question 6
book = run_query_select(f'SELECT title, name FROM books b INNER JOIN authors a ON a.id = b.author_id')
for row in book:
    print(row)

#question 7
try:
    book = run_update_query(f"INSERT INTO books VALUES (?,?,?,?)",(6,'Hear the wing sing',3,1990))
    print('success')
except Exception as e:
    print(f"failed to insert {e}")
