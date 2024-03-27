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
    parser = argparse.ArgumentParser(description='Scrape website for specific information and save in MySQL database.')
    parser.add_argument('--url', help='URL ', required=True)
    return parser.parse_args()

def create_mysql_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',  
            database='test' 
        )
        print("Connexion à MySQL DB réussie")
        return connection
    except Error as e:
        print(f"Erreur lors de la connexion à MySQL: {e}")
        return None

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS info_formation (
            id INT AUTO_INCREMENT PRIMARY KEY,
            information TEXT NOT NULL
        );
    ''')
    connection.commit()

def insert_information(connection, information):
    cursor = connection.cursor()
    query = "INSERT INTO info_formation (information) VALUES (%s)"
    cursor.execute(query, (information,))
    connection.commit()

def highlight(element):
    driver.execute_script("arguments[0].style.border='3px solid red'", element)

args = parse_arguments()

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get(args.url)
time.sleep(2)

accept_cookies(driver)
incremental_scroll(driver, increments=10, delay=1)
scroll_to_top(driver)

click_target_xpath = "/html/body/div[2]/section[3]/div/ul/li[2]"
click_target_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, click_target_xpath))
)
click_target_element.click()
time.sleep(2)

target_xpath = "/html/body/div[2]/section[3]/div/div/div[2]/div/p[7]"
target_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, target_xpath))
)
highlight(target_element)

info_div = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/section[3]/div/div/div[2]/div'))
)
paragraphs = info_div.find_elements(By.TAG_NAME, "p")

connection = create_mysql_connection()
if connection:
    create_table(connection)

for paragraph in paragraphs:
    highlight(paragraph)
    print("Information:", paragraph.text)
    if connection:
        insert_information(connection, paragraph.text)
    if paragraph == target_element:
        break

driver.quit()
if connection:
    connection.close()
