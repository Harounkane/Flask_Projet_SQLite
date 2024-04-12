CREATE TABLE livre (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titre TEXT NOT NULL,
    auteur TEXT NOT NULL,
    annee_publication INTEGER,
    genre TEXT,
    resume TEXT,
    disponible BOOLEAN NOT NULL DEFAULT 1
);
