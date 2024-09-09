#prueba 7
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def run():
    # Configuración del WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # Acceder a la página principal
        driver.get("https://www.recorrido.cl/es")

        # Navegar a la página de registro
        login_link = driver.find_element(By.XPATH, '//*[@id="login-toggle"]')
        login_link.click()
        time.sleep(3)

        # Ingresar un correo electrónico válido
        email_field = driver.find_element(By.XPATH, '//*[@id="new_user_email"]')
        email_field.clear()
        email_field.send_keys("rekaw8716@amxyy.com")

        # Ingresar una contraseña inválida
        password_field = driver.find_element(By.XPATH, '//*[@id="new_user_password"]')
        password_field.clear()
        password_field.send_keys("Clave12434")

        # Confirmar la contraseña
        confirm_password_field = driver.find_element(By.XPATH, '//*[@id="new_user_password_confirmation"]')
        confirm_password_field.clear()
        confirm_password_field.send_keys("Clave1234")

        # Esperar la intervención manual para el CAPTCHA
        input("Por favor, resuelve el CAPTCHA manualmente y presiona Enter para continuar...")

        WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="signup"]/form/div[3]/input'))
        )


        register_button = driver.find_element(By.XPATH, '//*[@id="signup"]/form/div[3]/input')
        register_button.click()


        time.sleep(5)

        return True, "Contraseñas no coinciden"

    finally:
        # Cerrar el navegador
        driver.quit()

