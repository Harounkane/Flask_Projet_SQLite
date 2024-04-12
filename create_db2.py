import sqlite3

connection = sqlite3.connect('database2.db')

with open('schema2.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO livre (titre, auteur, annee_publication, genre, resume, disponible) VALUES (?, ?, ?, ?, ?, ?)", 
            ('Le Petit Prince', 'Antoine de Saint-Exupéry', 1943, 'Conte philosophique', 
             'Un jeune prince explore différentes planètes et apprend des leçons de vie.', 1))

cur.execute("INSERT INTO livre (titre, auteur, annee_publication, genre, resume, disponible) VALUES (?, ?, ?, ?, ?, ?)", 
            ('Harry Potter à l\'École des Sorciers', 'J.K. Rowling', 1997, 'Fantasy', 
             'Un jeune sorcier découvre son héritage magique et affronte le mal.', 1))

cur.execute("INSERT INTO livre (titre, auteur, annee_publication, genre, resume, disponible) VALUES (?, ?, ?, ?, ?, ?)", 
            ('1984', 'George Orwell', 1949, 'Science-fiction', 
             'Dans une société totalitaire, un homme lutte pour sa liberté et sa vérité.', 1))

# Ajoutez d'autres INSERT INTO pour insérer plus de livres

connection.commit()
connection.close()
