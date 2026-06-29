# SQLAlchemy Training
Dans le cadre de mon stage à [**BP²I**](https://www.linkedin.com/company/bnp-paribas-partners-for-innovation/about/) pour valider ma 1ère année de BTS SIO SLAM, je me suis formé à l'utilisation de **SQLAlchemy** pour manipuler des bases de données relationnelles avec Python, afin de prendre en main le fonctionnement de leurs outils internes.

---

## Objectif du projet :

- Prendre en main SQLite et SQLAlchemy pour manipuler des bases de données relationnelles avec Python,
- Créer et gérer des sessions de connexion à une base de données,
- Exécuter des requêtes CRUD *(Create, Read, Update, Delete)*,
- Structurer une application Python avec une base de données,
- Comprendre le lien entre le code Python, les tables SQL et les relations entre elles,
- Gérer les dépendances et l'environnement virtuel du projet avec Poetry.
- Manipuler les données avec Alembic pour gérer les migrations de la base de données.

## Les langages utilisés dans le projet :

| Langage | Utilisation |
| --- | --- |
| <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" alt="Python" width="32"> | Langage utilisé principalement pour écrire les fonctions, lancer le programme et manipuler les données. |
| <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/sqlalchemy/sqlalchemy-original.svg" alt="SQLAlchemy" width="32"> | ORM Python pour le coeur du projet : il permet de manipuler des tables SQL avec du code Python. |
| <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/sqlite/sqlite-original.svg" alt="SQLite" width="32"> | Base de données locale, stockée dans le fichier [**`sqlalchemy_training.db`**](sqlalchemy_training.db). |

## Modèle de données travailés :

Le projet manipule trois tables principales :
```python
utilisateur
  id
  nom
  email

telephone
  id
  marque
  modele
  prix

favori
  utilisateur_id -> utilisateur.id
  telephone_id   -> telephone.id
```

## Organisation du code :
 
```md
Python
  -> connexion SQLite
  -> creation des tables
  -> insertion des telephones et utilisateurs
  -> recherche des identifiants
  -> ajout des favoris
  -> commit puis fermeture
```

## Fichiers principaux :

- Code Python : [**`src/sqlalchemy_training/main.py`**](src/sqlalchemy_training/main.py)
- Base de données : [**`sqlalchemy_training.db`**](sqlalchemy_training.db)

## Ressources utilisées pour le projet :

- Documentation Python : https://docs.python.org/3/
- Documentation SQLite : https://www.sqlite.org/docs.html
- Documentation SQLAlchemy : https://docs.sqlalchemy.org/
- Documentation Poetry : https://python-poetry.org/docs/
- Documentation Alembic : https://alembic.sqlalchemy.org/en/latest/

---

> Ce projet a été réalisé dans le cadre de mon stage à [**BP²I**](https://www.linkedin.com/company/bnp-paribas-partners-for-innovation/about/) pour valider ma 1ère année de BTS SIO SLAM du 22 juin au 31 juillet 2026.