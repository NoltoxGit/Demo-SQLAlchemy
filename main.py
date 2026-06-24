import sqlite3

connexion = sqlite3.connect("phones.db")
curseur = connexion.cursor()

curseur.execute("""
CREATE TABLE IF NOT EXISTS phones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    marque TEXT NOT NULL,
    type TEXT NOT NULL,
    prix INTEGER NOT NULL
)
""")

connexion.commit()
connexion.close()

print("La base de données vient d'être créée avec succès !")