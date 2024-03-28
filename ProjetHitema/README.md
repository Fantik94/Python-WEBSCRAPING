# ProjetHitema
## Auteur : RINGLER Baptiste (Fantik94)
## Objectif du projet

Le but de ce projet est de coder un script Python qui permet d'extraire automatiquement des informations ciblées du site web h3hitema.fr. Les informations extraites seront les formations proposées par cette école et d'autres informations liées.

## Spécifications

- Choisir un site comme source de données.
- Définir une problématique pertinente en lien avec les données ciblées.
- Utiliser un outil de scraping tel que BeautifulSoup (bs4) pour extraire les données. Dans notre cas c'est Selenium
- Documenter toutes les étapes de récupération des données dans un fichier Jupyter Notebook.
- Inclure des temps de pause dans le code pour éviter d'être signalé comme spam par le site.
- Fournir une documentation claire et concise dans le fichier README.md, expliquant les différentes lignes de code et comment exécuter le script.
- Enregistrer les données extraites dans une base de données (utilisation de MySQL dans ce projet).
- Afficher les tables de la base de données et effectuer une requête pour afficher les résultats.
- Emballer le script dans un conteneur Docker et fournir les commandes nécessaires pour exécuter le code dans le README.md à la racine du repo.

## Bonus (facultatif)

- Refactorer le code Jupyter en un script principal orienté objet en utilisant le module argparse pour permettre l'utilisation d'entrées utilisateur lors de l'exécution du script.
- Déployer le conteneur Docker dans une machine virtuelle Azure avec une adresse IP publique.
- Utiliser une base de données Azure pour stocker les résultats du scraping.
- Déployer le scraper dans Azure App Service.
- Surveiller les requêtes dans Azure et fournir une capture d'écran du tableau de bord de l'application en activité.

## Checklist du Projet

### Spécifications Principales
- [x] Choisir un site comme source de données.(https://h3hitema.fr), par ailleurs site nul 
- [x] Définir une problématique pertinente en lien avec les données ciblées. => A quel point nous ment-on ?
- [x] Utiliser Selenium comme outil  pour extraire les données.
- [x] Documenter les étapes de récupération des données dans un fichier Jupyter Notebook.
- [x] Inclure des temps de pause dans le code pour éviter d'être signalé comme spam par le site.
- [x] Enregistrer les données extraites dans une base de données MySQL.
- [x] Afficher les tables de la base de données et effectuer une requête pour afficher les résultats.
- [x] Emballer le script dans un conteneur Docker.

### Bonus (facultatif)
- [x] Refactorer le code Jupyter en un script principal orienté objet.
- [ ] Déployer le conteneur Docker dans une machine virtuelle Azure avec une adresse IP publique.
- [ ] Utiliser une base de données Azure pour stocker les résultats du scraping.
- [ ] Déployer le scraper dans Azure App Service.
- [ ] Surveiller les requêtes dans Azure et fournir une capture d'écran du tableau de bord de l'application en activité.

