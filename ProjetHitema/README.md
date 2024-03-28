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

## Extraction de Données

L'objectif de cette section est d'extraire automatiquement des informations sur les formations proposées par le site [h3hitema.fr](https://www.h3hitema.fr/formations-informatiques/) en utilisant Selenium.Il faut bien sur avoir installé Chrome et son driver. Voici les étapes principales du processus d'extraction :

1. **Installation des packages nécessaires :** On commence par installer Selenium et d'autres bibliothèques utiles pour le scraping et l'interaction avec les navigateurs web.
    ```python
    !pip install selenium webdriver-manager pandas sqlalchemy pymongo
    ```

2. **Initialisation du navigateur :** Utilisation de Selenium pour ouvrir une instance de Chrome et naviguer vers la page des formations informatiques de H3 Hitema.
    ```python
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.h3hitema.fr/formations-informatiques/")
    time.sleep(2)
    ```

3. **Gestion des cookies :** Acceptation des cookies pour permettre le chargement complet de la page.
    ```python
    cookie_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="cmplz-cookiebanner-container"]/div/div[6]/button[1]'))
    )
    cookie_button.click()
    ```

4. **Défilement incrémentiel :** Pour s'assurer que toutes les informations sont chargées sur la page, un défilement incrémentiel est effectué.
    ```python
    def incremental_scroll(driver, increments=10, delay=1):
        for i in range(increments):
            scroll_position = driver.execute_script("return document.body.scrollHeight") * (i+1) / increments
            driver.execute_script(f"window.scrollTo(0, {scroll_position});")
            time.sleep(delay)
    incremental_scroll(driver, increments=10, delay=1)
    ```

5. **Extraction des données :** On parcourt toutes les catégories de formations et pour chaque formation, on extrait le titre, les badges associés, une description et le lien vers la page de la formation.
    ```python
    main_div = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "list__formations"))
    )
    categories = main_div.find_elements(By.TAG_NAME, "h3")
    for category in categories:
        highlight(category)
        print(f"Catégorie: {category.text}\n{'-'*20}")
        ...
    ```

6. **Nettoyage :** Fermeture du navigateur après l'extraction des données.
    ```python
    driver.quit()
    ```

Ce script permet d'automatiser la récupération d'informations précieuses sur les formations proposées par H3 Hitema, pour savoir si cette école nous ment ou non.

## Exemple de Sortie

Voici un aperçu des informations extraites du site h3hitema.fr, illustrant les données recueillies concernant différentes formations disponibles. Cet exemple montre comment les informations sont structurées et présentées par le script.

```
Catégorie: BTS INFORMATIQUE (BAC+2)
Titre de la formation: BTS CIEL Cybersécurité
Badges: Aucun
Description: option IR
Lien de la formation: https://www.h3hitema.fr/formation/bts-cybersecurite-option-ir/
-----------
Titre de la formation: BTS SIO
Badges: ALTERNANCE, FORMATION INITIALE
Description: option SLAM
Lien de la formation: https://www.h3hitema.fr/formation/bts-sio-option-slam/
-----------
Titre de la formation: BTS SIO
Badges: ALTERNANCE, FORMATION INITIALE
Description: option SISR
Lien de la formation: https://www.h3hitema.fr/formation/bts-sio-option-sisr/
```