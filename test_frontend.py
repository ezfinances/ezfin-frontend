from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# inicia o Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # abre seu site React
    driver.get("http://localhost:3001")

    time.sleep(2)  # só pra ver a página carregar, seu apressado

    # Exemplo: pegar um botão
    btn = driver.find_element(By.XPATH, "//button")

    btn.click()

    time.sleep(2)

finally:
    driver.quit()
