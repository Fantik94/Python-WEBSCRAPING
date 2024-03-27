import argparse
import mysql.connector
from mysql.connector import Error
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Définition de la fonction pour analyser les arguments de ligne de commande
def parse_arguments():
    parser = argparse.ArgumentParser(description='Web scraper for formations.')
    parser.add_argument('--url', help='URL à webscrap', required=True)
    return parser.parse_args()

def create_mysql_connection():
    """Crée une connexion à la base de données MySQL."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',  
            database='test' 
        )
        print("Connexion à MySQL réussie")
        return connection
    except Error as e:
        print(f"Erreur lors de la connexion à MySQL: {e}")
        return None

def create_table(connection):
    """Crée la table formations si elle n'existe pas déjà."""
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS formations (
            id INT AUTO_INCREMENT PRIMARY KEY,
            categorie TEXT NOT NULL,
            titre TEXT NOT NULL,
            badges TEXT,
            description TEXT,
            lien TEXT NOT NULL
        );
    ''')
    connection.commit()

def insert_formation(connection, formation):
    """Insère une formation dans la base de données."""
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO formations (categorie, titre, badges, description, lien)
        VALUES (%s, %s, %s, %s, %s)
    ''', formation)
    connection.commit()

def highlight(element):
    """Surligne un élément web."""
    driver.execute_script("arguments[0].style.border='3px solid red'", element)

args = parse_arguments()

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get(args.url)
time.sleep(2)

cookie_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cmplz-cookiebanner-container"]/div/div[6]/button[1]')))
cookie_button.click()

def incremental_scroll(driver, increments=10, delay=1):
    for i in range(increments):
        scroll_position = driver.execute_script("return document.body.scrollHeight") * (i + 1) / increments
        driver.execute_script(f"window.scrollTo(0, {scroll_position});")
        time.sleep(delay)

incremental_scroll(driver, increments=10, delay=1)

connection = create_mysql_connection()
if connection is not None:
    create_table(connection)

main_div = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "list__formations")))
categories = main_div.find_elements(By.TAG_NAME, "h3")

for category in categories:
    highlight(category)
    
    formation_index = categories.index(category) + 1
    formation_cards = driver.find_elements(By.CSS_SELECTOR, f"div.slider--formations:nth-of-type({formation_index}) a.card-formation--small")

    for card in formation_cards:
        title_element = card.find_element(By.CLASS_NAME, "card-formation__title")
        highlight(title_element)
        title = title_element.text

        badge_list_elements = card.find_elements(By.CLASS_NAME, "list-badge")
        badges = ", ".join([badge.text for badge in badge_list_elements[0].find_elements(By.TAG_NAME, "span")]) if badge_list_elements else "Aucun"

        paragraph_element = card.find_elements(By.TAG_NAME, "p")
        paragraph = paragraph_element[0].text if paragraph_element else "Pas de description disponible"
        
        link = card.get_attribute('href')
        
        if connection is not None:
            insert_formation(connection, (category.text, title, badges, paragraph, link))

driver.quit()
if connection is not None:
    connection.close()
