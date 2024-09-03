#prueba 5 deelan "aun falta"
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

    # When: navego a la página de registro
    signup_link = driver.find_element(By.XPATH, '//*[@id="signup-tab"]')
    signup_link.click()

    time.sleep(3)  # Esperar a que la página de registro cargue completamente

    # And: ingreso un correo electrónico válido "rekaw87146@amxyy.com"
    email_field = driver.find_element(By.XPATH, '//*[@id="new_user_email"]')
    email_field.clear()
    email_field.send_keys("rekaw87146@amxyy.com")

    # And: ingreso una contraseña válida "Clave1234"
    password_field = driver.find_element(By.XPATH, '//*[@id="new_user_password"]')
    password_field.clear()
    password_field.send_keys("Clave1234")

    # And: confirmo la contraseña "Clave1234"
    confirm_password_field = driver.find_element(By.XPATH, '//*[@id="new_user_password_confirmation"]')
    confirm_password_field.clear()
    confirm_password_field.send_keys("Clave1234")

    # And: Valido el captcha
    captcha_checkbox = driver.find_element(By.XPATH, '//*[@id="recaptcha-anchor"]/div[1]')
    captcha_checkbox.click()

    time.sleep(5)  # Esperar a que el captcha se valide, si es necesario

    # And: hago clic en el botón de "Registrarse"
    register_button = driver.find_element(By.XPATH, '//*[@id="signup"]/form/div[3]/input')
    register_button.click()

    # Then: Se crea la cuenta y se envía un correo para activarla
    time.sleep(5)  # Esperar a que se complete el proceso de registro

    print("Registro completado exitosamente. Revisa tu correo para activar la cuenta.")

finally:
    # Cerrar el navegador
    driver.quit()
