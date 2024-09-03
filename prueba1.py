#prueba 1 Genaro
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuración del WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Given: que puedo acceder a la aplicación
    driver.get("https://www.recorrido.cl/es")  # URL de la página principal

    # When: puedo acceder al login
    login_link = driver.find_element(By.XPATH, '//*[@id="login-toggle"]')
    login_link.click()

    login_lin = driver.find_element(By.XPATH, '//*[@id="signin-tab"]')
    login_lin.click()
    
    time.sleep(3)  # Esperar a que la página de login cargue completamente
    
    # And: ingreso como usuario "fhlbkblgfaiapsoddc@hthlm.com" (10 minuteMail)
    email_field = driver.find_element(By.XPATH, '//*[@id="user_email"]')
    email_field.clear()
    email_field.send_keys("fhlbkblgfaiapsoddc@hthlm.com")

    # And: ingreso una clave incorrecta "clavenoesfalsa123"
    password_field = driver.find_element(By.XPATH, '//*[@id="user_password"]')
    password_field.clear()
    password_field.send_keys("clavenoesfalsa123")

    # And: realizo el envío de los datos
    login_button = driver.find_element(By.XPATH, '/html/body/header/nav/div/div[2]/ul[2]/li[3]/div/div[2]/div/div/div[1]/div/div/div[1]/form/div[3]/input')
    login_button.click()

    # Then: se inicia sesión y redirecciona al dashboard
    time.sleep(5)  # Esperar a que se complete la redirección

    # Verificar que la URL es la del dashboard
    assert "https://www.recorrido.cl/es/users/dashboard" in driver.current_url, "La URL no es la esperada"

    print("Test completado exitosamente.")

finally:
    # Cerrar el navegador
    driver.quit()
