import sqlite3

connexion = sqlite3.connect("phones.db")
curseur = connexion.cursor()

curseur.execute("""
CREATE TABLE IF NOT EXISTS phones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    marque TEXT NOT NULL,
    modele TEXT NOT NULL,
    prix INTEGER NOT NULL
)
""")

curseur.execute("""
INSERT INTO phones (marque, modele, prix)
VALUES (?, ?, ?)
""", ("Samsung", "Galaxy S24", 899))

connexion.commit()
connexion.close()

print("Téléphone ajouté avec succès !")